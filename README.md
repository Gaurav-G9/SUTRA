# 📚 Sutra - Daily Current Affairs Aggregator

**Sutra** is an intelligent daily current affairs compilation tool designed specifically for **UPSC/UPPSC exam preparation**. It aggregates content from major IAS coaching institutes and news portals, deduplicates information, and generates professional PDF reports in English or Hindi.

## 🎯 Features

- ✅ **Multi-Source Scraping**: Aggregates from 12+ major IAS coaching sites
- ✅ **News Portal Integration**: Collects from PIB, PTI, The Hindu, Indian Express, Times of India, etc.
- ✅ **Smart Deduplication**: Ensures no repeated content across sources
- ✅ **Comprehensive Coverage**: 30+ daily current affairs items with detailed explanations
- ✅ **Editorial Analysis**: Curated editorials and analytical pieces from all sources
- ✅ **Preliminary Exam Points**: 20+ static/dynamic points relevant for Prelims
- ✅ **Bilingual Support**: Toggle between English and Hindi for current affairs content
- ✅ **Professional PDF Generation**: English app interface with English/Hindi content output
- ✅ **Daily Automation**: Scheduled runs for automated compilation
- ✅ **Multi-Category Coverage**: Government schemes, policies, economy, environment, defence, international relations, science-tech, polity, geography, history, appointments, agreements, sports, ethics, and more

## 📋 Covered Sources

### IAS Coaching Institutes
- Vajiram & Ravi
- Drishti IAS
- Vision IAS
- PMFIAS
- IASBABA
- Chahal IAS
- Vajirao IAS
- NextIAS
- ForumIAS
- RAU'S IAS
- LearnThruPractice
- GK TODAY

### News Portals
- PIB (Press Information Bureau)
- PRS Legislative
- All India Radio (Akashvani)
- News On Air
- The Hindu
- Indian Express
- Times of India
- Lok Sabha TV
- And more...

## 🏗️ Project Structure

```
Sutra/
├── src/
│   ├── scrapers/              # Web scrapers for each source
│   │   ├── coaching_sites.py
│   │   ├── news_portals.py
│   │   └── scrapers_config.py
│   ├── aggregators/           # Data aggregation & deduplication
│   │   ├── content_aggregator.py
│   │   ├── deduplicator.py
│   │   └── categorizer.py
│   ├── nlp/                   # NLP for analysis
│   │   ├── summarizer.py
│   │   └── keyword_extractor.py
│   ├── pdf_generator/         # PDF generation
│   │   ├── pdf_builder.py
│   │   ├── templates/
│   │   └── styles/
│   ├── translator/            # Language translation (English <-> Hindi)
│   │   ├── translator.py
│   │   └── translation_cache.py
│   ├── database/              # Database models
│   │   ├── models.py
│   │   └── db_handler.py
│   └── utils/                 # Utility functions
│       ├── logger.py
│       ├── config_loader.py
│       └── constants.py
├── config/
│   ├── sources.yaml           # Source configurations
│   ├── categories.yaml        # Content categories
│   └── settings.py
├── templates/
│   ├── pdf_template.html      # HTML template for PDF
│   ├── pdf_template_hi.html   # HTML template for Hindi PDF
│   └── styles.css             # PDF styling
├── data/                      # Data storage
│   ├── raw/
│   ├── processed/
│   └── pdfs/
├── logs/                      # Application logs
├── tests/                     # Unit tests
├── docs/                      # Documentation
├── requirements.txt           # Python dependencies
├── main.py                    # Entry point
├── scheduler.py               # Scheduled tasks
└── .env.example               # Environment variables template
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip
- Virtual environment (recommended)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Gaurav-G9/Sutra.git
   cd Sutra
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment**
   ```bash
   cp .env.example .env
   # Edit .env with your settings
   # Set CURRENT_AFFAIRS_LANGUAGE to 'English' or 'Hindi'
   ```

5. **Run the aggregator**
   ```bash
   python main.py
   ```

6. **Schedule daily runs** (Optional)
   ```bash
   python scheduler.py
   ```

## 📖 Usage

### Generate Daily Current Affairs Report

```python
from src.aggregators.content_aggregator import ContentAggregator
from src.pdf_generator.pdf_builder import PDFBuilder

# Initialize aggregator
aggregator = ContentAggregator(language='English')  # or 'Hindi'

# Fetch and process data
daily_affairs = aggregator.compile_daily_affairs()

# Generate PDF
pdf_builder = PDFBuilder(language='English')
pdf_builder.generate(daily_affairs, output_path="output.pdf")
```

### Toggle Current Affairs Language

```python
# Change language in .env file
CURRENT_AFFAIRS_LANGUAGE=Hindi

# Or programmatically
from src.aggregators.content_aggregator import ContentAggregator

aggregator = ContentAggregator(language='Hindi')
affairs_in_hindi = aggregator.compile_daily_affairs()
```

### Configure Sources

Edit `config/sources.yaml` to add/remove sources or modify scraping parameters.

## 🔄 Workflow

```
1. Scrape Sources → 2. Parse Content → 3. Categorize → 4. Deduplicate 
→ 5. Summarize → 6. Extract Keywords → 7. Generate Prelim Points 
→ 8. Translate (if needed) → 9. Create PDF → 10. Store Data → 11. Notify Users
```

## 📊 Content Categories

- 📋 Government Schemes & Policies
- 💰 Economy & Finance
- 🌍 International Relations
- 🛡️ Defence & Security
- 🔬 Science & Technology
- 📜 Polity & Constitution
- 🗺️ Geography & Environment
- 📚 History & Culture
- 👔 Appointments & Organizations
- 📝 International Agreements
- ⚽ Sports
- 🤝 Ethics & Governance
- �� Other Important News

## 🔧 Configuration

### Environment Variables (.env)
```
APP_NAME=Sutra
APP_LANGUAGE=English
CURRENT_AFFAIRS_LANGUAGE=English  # Change to Hindi for Hindi output
GENERATE_BILINGUAL=True           # Generate both versions
DEBUG=False
LOG_LEVEL=INFO
DATABASE_URL=sqlite:///sutra.db
PDF_OUTPUT_DIR=./data/pdfs
ENABLE_SCHEDULER=True
SCHEDULER_TIME=06:00
```

### sources.yaml
```yaml
coaching_institutes:
  - name: vajiram_ravi
    url: https://www.vajiramandravi.com
    enabled: true
  - name: drishti_ias
    url: https://www.drishtiias.com
    enabled: true
  # ... more sources
```

## 📦 Dependencies

- **Web Scraping**: BeautifulSoup4, Scrapy, Selenium
- **Data Processing**: Pandas, NumPy
- **NLP**: NLTK, spaCy, transformers
- **PDF Generation**: WeasyPrint, Jinja2
- **Translation**: Google Translate API, Indic Transliteration
- **Database**: SQLAlchemy, SQLite
- **Scheduling**: APScheduler
- **API Clients**: Requests
- **Logging**: Python logging
- **Testing**: pytest

See `requirements.txt` for complete list.

## 🎓 Output Format

### PDF Report Structure (English or Hindi)
```
📄 Daily Current Affairs Report
├── 📅 Date & Metadata
├── 📌 Executive Summary
├── 📚 30+ Current Affairs Items
│   ├── Title & Source
│   ├── Detailed Explanation
│   ├── Relevance (Prelims/Mains)
│   ├── Keywords
│   └── Related Topics
├── ✏️ Editorial Section
│   ├── Key Arguments
│   ├── Analysis
│   └── Exam Relevance
├── 🎯 20+ Preliminary Exam Points
│   ├── Static/Dynamic Information
│   ├── Detailed Explanations
│   └── Interconnections
└── 📋 Index & Cross-References
```

## ⚙️ Advanced Features

- **Duplicate Detection**: Uses cosine similarity & semantic matching
- **Smart Summarization**: Extracts key points using extractive & abstractive summarization
- **Keyword Extraction**: Identifies important terms for quick revision
- **Trend Analysis**: Identifies recurring topics across sources
- **Historical Tracking**: Maintains archive for reference
- **Custom Filters**: Filter by category, source, date range
- **Email Notifications**: Automated daily email delivery
- **Bilingual Generation**: Automatic translation between English and Hindi
- **Web Dashboard**: View reports online (planned)

## 🔐 Legal & Ethical Considerations

- **Respectful Scraping**: Implements rate limiting and respects robots.txt
- **Attribution**: Proper credit given to all sources
- **Educational Purpose**: For exam preparation only
- **Terms of Service**: Complies with each source's ToS
- **User Privacy**: No personal data collection beyond necessary metadata

## 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📞 Support & Feedback

- 📧 Email: gaurav.g9@example.com
- 🐛 Issues: GitHub Issues
- 💬 Discussions: GitHub Discussions

## 🙏 Acknowledgments

- All IAS coaching institutes for quality educational content
- News portals for current affairs updates
- UPSC community for feedback and suggestions

## ⚠️ Disclaimer

This tool is created for educational purposes to aid UPSC/UPPSC exam preparation. Users are responsible for verifying information from official sources. The creators are not affiliated with any coaching institute or news portal.

---

**Made with ❤️ for UPSC Aspirants** | Last Updated: September 2026
