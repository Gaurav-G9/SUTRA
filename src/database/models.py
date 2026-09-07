"""
Database Models for Sutra Application
"""

from datetime import datetime
from sqlalchemy import Column, String, Text, DateTime, Integer, Float, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Source(Base):
    """Model for content sources"""
    __tablename__ = 'sources'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True, nullable=False)
    url = Column(String(500), nullable=False)
    source_type = Column(String(100), nullable=False)  # Coaching Institute, News Portal, etc.
    enabled = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    articles = relationship('Article', back_populates='source')
    
    def __repr__(self):
        return f"<Source(name='{self.name}', type='{self.source_type}')>"


class Article(Base):
    """Model for scraped articles/current affairs"""
    __tablename__ = 'articles'
    
    id = Column(Integer, primary_key=True)
    source_id = Column(Integer, ForeignKey('sources.id'), nullable=False)
    title = Column(String(500), nullable=False)
    content = Column(Text, nullable=False)
    summary = Column(Text)
    url = Column(String(1000))
    category = Column(String(100), nullable=False)
    language = Column(String(50), default='English')  # English or Hindi
    keywords = Column(Text)  # Comma-separated keywords
    exam_relevance = Column(String(50))  # Prelims, Mains, Both
    is_duplicate = Column(Boolean, default=False)
    similarity_score = Column(Float)  # For deduplication
    scraped_at = Column(DateTime, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    source = relationship('Source', back_populates='articles')
    compilation_items = relationship('CompilationItem', back_populates='article')
    
    def __repr__(self):
        return f"<Article(title='{self.title[:50]}...', category='{self.category}')>"


class DailyCompilation(Base):
    """Model for daily current affairs compilations"""
    __tablename__ = 'daily_compilations'
    
    id = Column(Integer, primary_key=True)
    compilation_date = Column(String(10), unique=True, nullable=False)  # YYYY-MM-DD
    language = Column(String(50), nullable=False)  # English or Hindi
    total_items = Column(Integer, default=0)
    total_editorials = Column(Integer, default=0)
    total_prelim_points = Column(Integer, default=0)
    pdf_path = Column(String(1000))
    pdf_generated = Column(Boolean, default=False)
    is_published = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    items = relationship('CompilationItem', back_populates='compilation')
    editorials = relationship('Editorial', back_populates='compilation')
    prelim_points = relationship('PrelimPoint', back_populates='compilation')
    
    def __repr__(self):
        return f"<DailyCompilation(date='{self.compilation_date}', language='{self.language}', items={self.total_items})>"


class CompilationItem(Base):
    """Model for items in daily compilation"""
    __tablename__ = 'compilation_items'
    
    id = Column(Integer, primary_key=True)
    compilation_id = Column(Integer, ForeignKey('daily_compilations.id'), nullable=False)
    article_id = Column(Integer, ForeignKey('articles.id'), nullable=False)
    item_order = Column(Integer)  # Order in the compilation
    section = Column(String(100))  # Current Affairs, Key Points, etc.
    explanation = Column(Text)  # Detailed explanation
    added_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    compilation = relationship('DailyCompilation', back_populates='items')
    article = relationship('Article', back_populates='compilation_items')
    
    def __repr__(self):
        return f"<CompilationItem(compilation_id={self.compilation_id}, order={self.item_order})>"


class Editorial(Base):
    """Model for editorial analysis and pieces"""
    __tablename__ = 'editorials'
    
    id = Column(Integer, primary_key=True)
    compilation_id = Column(Integer, ForeignKey('daily_compilations.id'), nullable=False)
    title = Column(String(500), nullable=False)
    source = Column(String(255))
    content = Column(Text, nullable=False)
    key_arguments = Column(Text)  # JSON or comma-separated
    analysis = Column(Text)
    exam_relevance = Column(String(50))  # Prelims, Mains, Both
    language = Column(String(50), default='English')
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    compilation = relationship('DailyCompilation', back_populates='editorials')
    
    def __repr__(self):
        return f"<Editorial(title='{self.title[:50]}...')>"


class PrelimPoint(Base):
    """Model for preliminary exam points"""
    __tablename__ = 'prelim_points'
    
    id = Column(Integer, primary_key=True)
    compilation_id = Column(Integer, ForeignKey('daily_compilations.id'), nullable=False)
    point_number = Column(Integer)  # Point number (1-20+)
    topic = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    is_static = Column(Boolean, default=False)  # Static or dynamic point
    related_articles = Column(Text)  # Article IDs or titles
    language = Column(String(50), default='English')
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    compilation = relationship('DailyCompilation', back_populates='prelim_points')
    
    def __repr__(self):
        return f"<PrelimPoint(topic='{self.topic}', point={self.point_number})>"


class UserPreference(Base):
    """Model for user preferences"""
    __tablename__ = 'user_preferences'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(String(100), unique=True, nullable=False)
    preferred_language = Column(String(50), default='English')  # English or Hindi
    preferred_categories = Column(Text)  # Comma-separated categories
    preferred_sources = Column(Text)  # Comma-separated sources
    email_notification = Column(Boolean, default=False)
    email_address = Column(String(255))
    notification_time = Column(String(5))  # HH:MM format
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f"<UserPreference(user_id='{self.user_id}', language='{self.preferred_language}')>"


class ScrapingLog(Base):
    """Model for scraping activity logs"""
    __tablename__ = 'scraping_logs'
    
    id = Column(Integer, primary_key=True)
    source_id = Column(Integer, ForeignKey('sources.id'))
    status = Column(String(50))  # Success, Failed, Partial
    items_scraped = Column(Integer, default=0)
    items_processed = Column(Integer, default=0)
    items_duplicated = Column(Integer, default=0)
    error_message = Column(Text)
    started_at = Column(DateTime, nullable=False)
    completed_at = Column(DateTime)
    duration_seconds = Column(Integer)
    
    def __repr__(self):
        return f"<ScrapingLog(source_id={self.source_id}, status='{self.status}')>"
