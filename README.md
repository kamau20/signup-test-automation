# Sign-Up Form Test Automation 🧪

Automated testing suite for a sign-up form using Python, Pytest, and Selenium WebDriver.

## 📋 Test Cases Covered

| # | Test Case | Status |
|---|-----------|--------|
| 1 | Successful account creation with all fields | ✅ Pass |
| 2 | Successful account creation without optional email | ✅ Pass |
| 3 | Password length validation (minimum 8 characters) | ✅ Pass |
| 4 | Password mismatch validation | ✅ Pass |
| 5 | Missing required field: Full Name | ✅ Pass |
| 6 | Missing required field: Phone Number | ✅ Pass |
| 7 | Invalid email format validation | ✅ Pass |
| 8 | All required fields empty validation | ✅ Pass |

## 🛠️ Technologies Used

- **Python 3.14**
- **Pytest** - Testing framework
- **Selenium WebDriver** - Browser automation
- **WebDriver Manager** - Automatic driver management
- **Chrome** - Browser for testing

## 📦 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- Chrome browser installed
- pip (Python package manager)

### Setup Instructions

1. **Clone the repository:**
```bash
git clone https://github.com/kamau20/signup-test-automation.git
cd signup-test-automation
```

2. **Create and activate virtual environment:**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

## 🚀 Running Tests

### Run all tests:
```bash
pytest tests/test_signup_form.py -v
```

### Run specific test:
```bash
pytest tests/test_signup_form.py::TestSignUpForm::test_01_successful_account_creation_all_fields -v
```

### Generate HTML report:
```bash
pytest tests/test_signup_form.py --html=reports/report.html --self-contained-html
```

### Run tests with detailed output:
```bash
pytest tests/test_signup_form.py -v -s
```

## 📁 Project Structure
```
SignUpTestAutomation/
│
├── tests/
│   ├── __init__.py
│   └── test_signup_form.py      # Main test file with 8 test cases
│
├── utils/
│   └── __init__.py
│
├── reports/                      # Generated HTML reports
│
├── signup_form.html              # Test page (sign-up form)
├── .gitignore
├── pytest.ini
├── requirements.txt
└── README.md
```

## 🧪 Test Scenarios

### Positive Tests
- ✅ Valid form submission with all fields
- ✅ Valid form submission without optional email

### Negative Tests
- ❌ Password less than 8 characters
- ❌ Password mismatch
- ❌ Empty required fields
- ❌ Invalid email format

### Validation Tests
- 🔍 Required field validation
- 🔍 Password strength validation
- 🔍 Email format validation
- 🔍 Password matching validation

## 📊 Test Results

All tests are passing successfully! ✅
```
tests/test_signup_form.py::TestSignUpForm::test_01... PASSED [ 12%]
tests/test_signup_form.py::TestSignUpForm::test_02... PASSED [ 25%]
tests/test_signup_form.py::TestSignUpForm::test_03... PASSED [ 37%]
tests/test_signup_form.py::TestSignUpForm::test_04... PASSED [ 50%]
tests/test_signup_form.py::TestSignUpForm::test_05... PASSED [ 62%]
tests/test_signup_form.py::TestSignUpForm::test_06... PASSED [ 75%]
tests/test_signup_form.py::TestSignUpForm::test_07... PASSED [ 87%]
tests/test_signup_form.py::TestSignUpForm::test_08... PASSED [100%]

========================= 8 passed in 45.23s =========================
```

## 🔧 Configuration

### pytest.ini
The project uses pytest configuration for:
- Test discovery patterns
- HTML report generation
- Verbose output

### Browser Configuration
- Default browser: Chrome
- WebDriver: Automatically managed via webdriver-manager
- Wait time: 10 seconds explicit wait

## 📝 Best Practices Implemented

- ✅ Page Object Model ready structure
- ✅ Explicit waits for stability
- ✅ Clear test naming convention
- ✅ Comprehensive error handling
- ✅ Reusable helper methods
- ✅ Fixture-based setup/teardown

## 🎯 Future Enhancements

- [ ] Implement Page Object Model
- [ ] Add data-driven testing with CSV/Excel
- [ ] Cross-browser testing (Firefox, Edge)
- [ ] Parallel test execution
- [ ] CI/CD integration (GitHub Actions)
- [ ] API testing integration
- [ ] Screenshot on failure

## 👤 Author

**[Your Name]**
- GitHub: [@yourusername](https://github.com/yourusername)
- LinkedIn: [Your Profile](https://linkedin.com/in/yourprofile)
- Email: your.email@example.com

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- Built with Python and Selenium
- Testing framework: Pytest
