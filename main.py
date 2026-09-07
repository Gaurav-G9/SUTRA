"""
Sutra - Daily Current Affairs Aggregator
Main entry point for the application
"""

import os
import sys
from datetime import datetime
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent))

from src.config.config_loader import ConfigLoader
from src.database.db_handler import DatabaseHandler
from src.aggregators.content_aggregator import ContentAggregator
from src.pdf_generator.pdf_builder import PDFBuilder
from src.utils.logger import setup_logger

# Initialize logger
logger = setup_logger(__name__)


class SutraApp:
    """Main Sutra Application Class"""
    
    def __init__(self):
        """Initialize the Sutra application"""
        self.config = ConfigLoader()
        self.db = DatabaseHandler(self.config.get('DATABASE_URL'))
        self.logger = logger
        
        self.logger.info(f"Sutra Application initialized")
        self.logger.info(f"App Language: {self.config.get('APP_LANGUAGE')}")
        self.logger.info(f"Current Affairs Language: {self.config.get('CURRENT_AFFAIRS_LANGUAGE')}")
    
    def run(self, language=None):
        """
        Run the daily current affairs aggregation and PDF generation
        
        Args:
            language (str): Language for current affairs ('English' or 'Hindi')
                          If None, uses value from .env
        """
        try:
            # Use provided language or get from config
            affairs_language = language or self.config.get('CURRENT_AFFAIRS_LANGUAGE', 'English')
            
            self.logger.info(f"Starting Sutra aggregation - Language: {affairs_language}")
            
            # Initialize aggregator
            aggregator = ContentAggregator(language=affairs_language)
            
            # Compile daily affairs
            self.logger.info("Compiling daily current affairs...")
            daily_affairs = aggregator.compile_daily_affairs()
            
            if not daily_affairs:
                self.logger.warning("No current affairs data compiled")
                return False
            
            self.logger.info(f"Successfully compiled {len(daily_affairs.get('items', []))} items")
            
            # Generate PDF
            self.logger.info("Generating PDF report...")
            pdf_builder = PDFBuilder(language=affairs_language)
            
            # Create output directory if not exists
            output_dir = Path(self.config.get('PDF_OUTPUT_DIR', './data/pdfs'))
            output_dir.mkdir(parents=True, exist_ok=True)
            
            # Generate filename with date
            date_str = datetime.now().strftime('%Y-%m-%d')
            filename = f"Sutra_CurrentAffairs_{date_str}_{affairs_language[:3].upper()}.pdf"
            output_path = output_dir / filename
            
            # Build and save PDF
            pdf_builder.generate(daily_affairs, str(output_path))
            
            self.logger.info(f"PDF generated successfully: {output_path}")
            
            # Store metadata in database
            self.db.save_compilation(
                date=date_str,
                language=affairs_language,
                items_count=len(daily_affairs.get('items', [])),
                pdf_path=str(output_path)
            )
            
            self.logger.info("Daily compilation completed successfully")
            return True
            
        except Exception as e:
            self.logger.error(f"Error during aggregation: {str(e)}", exc_info=True)
            return False
    
    def run_bilingual(self):
        """Generate reports in both English and Hindi"""
        self.logger.info("Starting bilingual report generation...")
        
        results = {
            'English': self.run('English'),
            'Hindi': self.run('Hindi')
        }
        
        self.logger.info(f"Bilingual generation completed - Results: {results}")
        return results
    
    def run_with_filters(self, language=None, categories=None, sources=None):
        """
        Run with custom filters
        
        Args:
            language (str): Language for output
            categories (list): Specific categories to include
            sources (list): Specific sources to scrape
        """
        try:
            affairs_language = language or self.config.get('CURRENT_AFFAIRS_LANGUAGE', 'English')
            
            self.logger.info(f"Starting filtered aggregation - Language: {affairs_language}")
            
            aggregator = ContentAggregator(
                language=affairs_language,
                categories=categories,
                sources=sources
            )
            
            daily_affairs = aggregator.compile_daily_affairs()
            
            pdf_builder = PDFBuilder(language=affairs_language)
            output_dir = Path(self.config.get('PDF_OUTPUT_DIR', './data/pdfs'))
            output_dir.mkdir(parents=True, exist_ok=True)
            
            date_str = datetime.now().strftime('%Y-%m-%d')
            filename = f"Sutra_Filtered_{date_str}_{affairs_language[:3].upper()}.pdf"
            output_path = output_dir / filename
            
            pdf_builder.generate(daily_affairs, str(output_path))
            
            self.logger.info(f"Filtered PDF generated: {output_path}")
            return True
            
        except Exception as e:
            self.logger.error(f"Error during filtered aggregation: {str(e)}", exc_info=True)
            return False


def main():
    """Main entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Sutra - Daily Current Affairs Aggregator for UPSC/UPPSC Exam Preparation'
    )
    
    parser.add_argument(
        '--language', '-l',
        choices=['English', 'Hindi'],
        help='Language for current affairs output (English or Hindi)'
    )
    
    parser.add_argument(
        '--bilingual', '-b',
        action='store_true',
        help='Generate reports in both English and Hindi'
    )
    
    parser.add_argument(
        '--categories', '-c',
        nargs='+',
        help='Specific categories to include (space-separated)'
    )
    
    parser.add_argument(
        '--sources', '-s',
        nargs='+',
        help='Specific sources to scrape (space-separated)'
    )
    
    parser.add_argument(
        '--filtered', '-f',
        action='store_true',
        help='Run with filters (requires --categories or --sources)'
    )
    
    args = parser.parse_args()
    
    # Initialize app
    app = SutraApp()
    
    # Run based on arguments
    if args.bilingual:
        app.run_bilingual()
    elif args.filtered and (args.categories or args.sources):
        app.run_with_filters(
            language=args.language,
            categories=args.categories,
            sources=args.sources
        )
    else:
        app.run(language=args.language)


if __name__ == '__main__':
    main()
