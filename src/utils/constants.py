"""Application Constants and Enumerations"""

from enum import Enum


class Language(Enum):
    """Supported languages"""
    ENGLISH = 'English'
    HINDI = 'Hindi'


class ContentCategory(Enum):
    """Content categories for current affairs"""
    GOVERNMENT_SCHEMES = 'Government Schemes & Policies'
    ECONOMY = 'Economy & Finance'
    INTERNATIONAL_RELATIONS = 'International Relations'
    DEFENCE = 'Defence & Security'
    SCIENCE_TECH = 'Science & Technology'
    POLITY = 'Polity & Constitution'
    GEOGRAPHY = 'Geography & Environment'
    HISTORY = 'History & Culture'
    APPOINTMENTS = 'Appointments & Organizations'
    AGREEMENTS = 'International Agreements'
    SPORTS = 'Sports'
    ETHICS = 'Ethics & Governance'
    OTHER = 'Other Important News'


class SourceType(Enum):
    """Types of content sources"""
    COACHING_INSTITUTE = 'Coaching Institute'
    NEWS_PORTAL = 'News Portal'
    OFFICIAL_GOVERNMENT = 'Official Government'


class ExamType(Enum):
    """Exam types"""
    PRELIMS = 'Prelims'
    MAINS = 'Mains'
    BOTH = 'Both'


# Source Configurations
COACHING_SOURCES = {
    'vajiram_ravi': {
        'name': 'Vajiram & Ravi',
        'url': 'https://www.vajiramandravi.com',
        'type': 'Coaching Institute'
    },
    'drishti_ias': {
        'name': 'Drishti IAS',
        'url': 'https://www.drishtiias.com',
        'type': 'Coaching Institute'
    },
    'vision_ias': {
        'name': 'Vision IAS',
        'url': 'https://www.visionias.in',
        'type': 'Coaching Institute'
    },
    'pmfias': {
        'name': 'PMFIAS',
        'url': 'https://www.pmfias.com',
        'type': 'Coaching Institute'
    },
    'iasbaba': {
        'name': 'IASBABA',
        'url': 'https://www.iasbaba.com',
        'type': 'Coaching Institute'
    },
    'chahal_ias': {
        'name': 'Chahal IAS',
        'url': 'https://www.chhalias.com',
        'type': 'Coaching Institute'
    },
    'vajirao_ias': {
        'name': 'Vajirao IAS',
        'url': 'https://www.vajiraoias.com',
        'type': 'Coaching Institute'
    },
    'nextias': {
        'name': 'NextIAS',
        'url': 'https://www.nextias.com',
        'type': 'Coaching Institute'
    },
    'forum_ias': {
        'name': 'ForumIAS',
        'url': 'https://www.forumias.com',
        'type': 'Coaching Institute'
    },
    'raus_ias': {
        'name': "RAU'S IAS",
        'url': 'https://www.rausias.com',
        'type': 'Coaching Institute'
    },
    'learn_thru_practice': {
        'name': 'LearnThruPractice',
        'url': 'https://www.learnthrupractice.com',
        'type': 'Coaching Institute'
    },
    'gk_today': {
        'name': 'GK TODAY',
        'url': 'https://www.gktoday.in',
        'type': 'Coaching Institute'
    }
}

NEWS_SOURCES = {
    'pib': {
        'name': 'Press Information Bureau',
        'url': 'https://pib.gov.in',
        'type': 'Official Government'
    },
    'prs': {
        'name': 'PRS Legislative',
        'url': 'https://www.prsindia.org',
        'type': 'Official Government'
    },
    'akashvani': {
        'name': 'All India Radio (Akashvani)',
        'url': 'https://www.newsonair.com',
        'type': 'Official Government'
    },
    'newsonair': {
        'name': 'News On Air',
        'url': 'https://www.newsonair.gov.in',
        'type': 'Official Government'
    },
    'thehindu': {
        'name': 'The Hindu',
        'url': 'https://www.thehindu.com',
        'type': 'News Portal'
    },
    'indianexpress': {
        'name': 'Indian Express',
        'url': 'https://www.indianexpress.com',
        'type': 'News Portal'
    },
    'toi': {
        'name': 'Times of India',
        'url': 'https://www.timesofindia.com',
        'type': 'News Portal'
    },
    'loksatta': {
        'name': 'Lok Sabha TV',
        'url': 'https://loksabhatv.an.gov.in',
        'type': 'Official Government'
    }
}

# Request Headers
DEFAULT_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}

# Timeout configurations
REQUEST_TIMEOUT = 30
RETRY_ATTEMPTS = 3
RETRY_DELAY = 5

# Rate limiting
RATE_LIMIT_DELAY = 2  # seconds between requests

# Content processing
MIN_CONTENT_LENGTH = 100
MAX_CONTENT_LENGTH = 5000
DEDUPLICATION_THRESHOLD = 0.85  # Cosine similarity threshold
SUMMARY_LENGTH = 150  # Number of words in summary

# PDF Configuration
PDF_PAPER_SIZE = 'A4'
PDF_MARGINS = {
    'top': 10,
    'bottom': 10,
    'left': 10,
    'right': 10
}
PDF_FONT_SIZE = 11
PDF_LINE_HEIGHT = 1.5

# Cache
CACHE_EXPIRY_HOURS = 24

# API Response Status
class APIStatus(Enum):
    """API response status codes"""
    SUCCESS = 'success'
    ERROR = 'error'
    PENDING = 'pending'
