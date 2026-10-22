import os
from dotenv import load_dotenv

load_dotenv()

# --- DO NOT MODIFY THE BELOW SECTION ---

# =================================================================
# 1. CORE SYSTEM CONFIGURATION (Do Not Modify)
# =================================================================
SUPABASE_URL: str = os.environ.get("SUPABASE_URL")
SUPABASE_SERVICE_ROLE_KEY: str = os.environ.get("SUPABASE_SERVICE_ROLE_KEY")
SUPABASE_TABLE_NAME: str = "jobs"
SUPABASE_CUSTOMIZED_RESUMES_TABLE_NAME = "customized_resumes"
SUPABASE_STORAGE_BUCKET = "personalized_resumes"
SUPABASE_RESUME_STORAGE_BUCKET = "resumes"
SUPABASE_BASE_RESUME_TABLE_NAME = "base_resume"
SUPABASE_RESUME_STYLE_TABLE_NAME = "resume_style_settings"
BASE_RESUME_PATH = "resume.json"

# API keys — set only the key(s) needed for your chosen provider.
LLM_API_KEY = (
    os.environ.get("LLM_API_KEY")
    or os.environ.get("FIREWORKS_API_KEY")
    or os.environ.get("FIREWORKS_AI_API_KEY")
    or os.environ.get("GEMINI_API_KEY")
    or os.environ.get("GEMINI_FIRST_API_KEY")
)

# =================================================================
# 2. USER PREFERENCES (Editable)
# =================================================================

# --- LLM Settings ---
# Use any model supported by LiteLLM (gemini, openai/gpt-4o-mini, groq/llama-3.3-70b-versatile)
# Full list of supported models & naming: https://docs.litellm.ai/docs/providers
LLM_MODEL = os.environ.get("LLM_MODEL") or "gemini"

# --- Search Configuration ---
LINKEDIN_SEARCH_QUERIES = [
    "Civil Engineer",
    "Technical Office Engineer",
    "Quantity Surveyor",
    "Infrastructure Engineer",
    "GRC Technical Office Engineer",
]

LINKEDIN_LOCATION = "Dubai"
LINKEDIN_GEO_ID = 100205264
LINKEDIN_JOB_TYPE = "F"
LINKEDIN_JOB_POSTING_DATE = "r604800"
LINKEDIN_F_WT = "1,2,3"

CAREERS_FUTURE_SEARCH_QUERIES = [
    "Civil Engineer",
    "Technical Office Engineer",
    "Quantity Surveyor",
    "Infrastructure Engineer",
]

CAREERS_FUTURE_SEARCH_CATEGORIES = ["Engineering"]
CAREERS_FUTURE_SEARCH_EMPLOYMENT_TYPES = ["Full Time"]
# =================================================================
# 3. ADVANCED SYSTEM SETTINGS (Modify with Caution)
# =================================================================
LLM_MAX_RPM = 10
LLM_MAX_RETRIES = 3
LLM_RETRY_BASE_DELAY = 10
LLM_DAILY_REQUEST_BUDGET = 0
LLM_REQUEST_DELAY_SECONDS = 8

LINKEDIN_MAX_START = 25 
REQUEST_TIMEOUT = 30
MAX_RETRIES = 3
RETRY_DELAY_SECONDS = 60          # Base cool-down on HTTP 429
DETAIL_FETCH_MIN_DELAY = 12.0     # Minimum delay between detail requests (seconds)
DETAIL_FETCH_MAX_DELAY = 22.0     # Maximum delay between detail requests (seconds)
SEARCH_QUERY_MIN_DELAY = 15.0     # Delay between search queries in standalone runs (seconds)
SEARCH_QUERY_MAX_DELAY = 30.0

JOB_EXPIRY_DAYS = 30
JOB_CHECK_DAYS = 3
JOB_DELETION_DAYS = 60
JOB_CHECK_LIMIT = 50
ACTIVE_CHECK_TIMEOUT = 20
ACTIVE_CHECK_MAX_RETRIES = 2
ACTIVE_CHECK_RETRY_DELAY = 10
