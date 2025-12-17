"""
Sign Up Form Test Automation using pytest and Selenium
Test cases for validating sign-up form functionality
"""

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time


class TestSignUpForm:
    """Test suite for Sign Up Form validation"""

    @pytest.fixture(autouse=True)
    def setup_and_teardown(self):
        """Setup and teardown for each test"""
        # Setup - runs before each test
        self.driver = webdriver.Chrome()  # or webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("file:///C:/Users/kamau/PycharmProjects/PythonProject/PythonProject/PythonProject/SignUpTestAutomation/signup_form.html")  # Replace with actual URL
        self.wait = WebDriverWait(self.driver, 10)

        yield  # This is where the test runs

        # Teardown - runs after each test
        self.driver.quit()

    def fill_form(self, full_name="", phone="", email="", password="", confirm_password=""):
        """Helper method to fill the sign-up form"""
        if full_name:
            name_field = self.driver.find_element(By.ID, "fullName")  # Adjust selector
            name_field.clear()
            name_field.send_keys(full_name)

        if phone:
            phone_field = self.driver.find_element(By.ID, "phoneNumber")  # Adjust selector
            phone_field.clear()
            phone_field.send_keys(phone)

        if email:
            email_field = self.driver.find_element(By.ID, "email")  # Adjust selector
            email_field.clear()
            email_field.send_keys(email)

        if password:
            password_field = self.driver.find_element(By.ID, "password")  # Adjust selector
            password_field.clear()
            password_field.send_keys(password)

        if confirm_password:
            confirm_field = self.driver.find_element(By.ID, "confirmPassword")  # Adjust selector
            confirm_field.clear()
            confirm_field.send_keys(confirm_password)

    def click_create_account(self):
        """Helper method to click Create Account button"""
        create_btn = self.driver.find_element(By.ID, "createAccountBtn")  # Adjust selector
        create_btn.click()
        time.sleep(2)  # Wait for response

    def test_01_successful_account_creation_all_fields(self):
        """Test Case 1: Verify successful account creation with all fields"""
        # Fill all fields with valid data
        self.fill_form(
            full_name="John Doe",
            phone="+254712345678",
            email="john.doe@example.com",
            password="Pass1234",
            confirm_password="Pass1234"
        )

        # Click Create Account button
        self.click_create_account()

        # Verify success message or redirection
        try:
            success_msg = self.wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "success-message"))
            )
            assert "success" in success_msg.text.lower() or "created" in success_msg.text.lower()
            print("✓ Test 1 Passed: Account created successfully with all fields")
        except TimeoutException:
            # Check if redirected to dashboard/home page
            assert "dashboard" in self.driver.current_url.lower() or "home" in self.driver.current_url.lower()
            print("✓ Test 1 Passed: Redirected to dashboard")

    def test_02_successful_account_without_email(self):
        """Test Case 2: Verify successful account creation without optional email"""
        # Fill required fields only (no email)
        self.fill_form(
            full_name="Jane Smith",
            phone="+254723456789",
            email="",  # Leave email empty
            password="Secret123",
            confirm_password="Secret123"
        )

        # Click Create Account button
        self.click_create_account()

        # Verify success
        try:
            success_msg = self.wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "success-message"))
            )
            assert success_msg.is_displayed()
            print("✓ Test 2 Passed: Account created without email")
        except TimeoutException:
            assert "dashboard" in self.driver.current_url.lower()
            print("✓ Test 2 Passed: Account created and redirected")

    def test_03_password_less_than_minimum_length(self):
        """Test Case 3: Verify error when password is less than 8 characters"""
        # Fill form with short password
        self.fill_form(
            full_name="Mike Wilson",
            phone="+254734567890",
            email="mike@example.com",
            password="Pass12",  # Only 6 characters
            confirm_password="Pass12"
        )

        # Click Create Account button
        self.click_create_account()

        # Verify error message
        error_msg = self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "error-message"))
        )
        assert "8 character" in error_msg.text.lower() or "minimum" in error_msg.text.lower()
        print("✓ Test 3 Passed: Password length validation working")

    def test_04_password_mismatch(self):
        """Test Case 4: Verify error when passwords do not match"""
        # Fill form with mismatched passwords
        self.fill_form(
            full_name="Sarah Johnson",
            phone="+254745678901",
            email="sarah@example.com",
            password="Password123",
            confirm_password="Password456"  # Different password
        )

        # Click Create Account button
        self.click_create_account()

        # Verify error message
        error_msg = self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "error-message"))
        )
        assert "match" in error_msg.text.lower() or "same" in error_msg.text.lower()
        print("✓ Test 4 Passed: Password mismatch validation working")

    def test_05_missing_full_name(self):
        """Test Case 5: Verify error when full name is empty"""
        # Fill form without full name
        self.fill_form(
            full_name="",  # Empty name
            phone="+254756789012",
            email="test@example.com",
            password="MyPass123",
            confirm_password="MyPass123"
        )

        # Click Create Account button
        self.click_create_account()

        # Verify error message
        error_msg = self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "error-message"))
        )
        assert "name" in error_msg.text.lower() and "required" in error_msg.text.lower()
        print("✓ Test 5 Passed: Full name validation working")

    def test_06_missing_phone_number(self):
        """Test Case 6: Verify error when phone number is empty"""
        # Fill form without phone number
        self.fill_form(
            full_name="David Brown",
            phone="",  # Empty phone
            email="david@example.com",
            password="Secure987",
            confirm_password="Secure987"
        )

        # Click Create Account button
        self.click_create_account()

        # Verify error message
        error_msg = self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "error-message"))
        )
        assert "phone" in error_msg.text.lower() and "required" in error_msg.text.lower()
        print("✓ Test 6 Passed: Phone number validation working")

    def test_07_invalid_email_format(self):
        """Test Case 7: Verify error when email format is invalid"""
        # Fill form with invalid email
        self.fill_form(
            full_name="Emily Davis",
            phone="+254767890123",
            email="invalidemail.com",  # Invalid format
            password="TestPass1",
            confirm_password="TestPass1"
        )

        # Click Create Account button
        self.click_create_account()

        # Verify error message
        error_msg = self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "error-message"))
        )
        assert "email" in error_msg.text.lower() and (
                    "valid" in error_msg.text.lower() or "format" in error_msg.text.lower())
        print("✓ Test 7 Passed: Email format validation working")

    def test_08_all_required_fields_empty(self):
        """Test Case 8: Verify errors when all required fields are empty"""
        # Don't fill any fields
        self.fill_form(
            full_name="",
            phone="",
            email="",
            password="",
            confirm_password=""
        )

        # Click Create Account button
        self.click_create_account()

        # Verify multiple error messages
        error_messages = self.driver.find_elements(By.CLASS_NAME, "error-message")
        assert len(error_messages) >= 4  # At least 4 required fields should show errors

        # Verify specific error messages
        error_texts = [msg.text.lower() for msg in error_messages]
        assert any("name" in text and "required" in text for text in error_texts)
        assert any("phone" in text and "required" in text for text in error_texts)
        assert any("password" in text and "required" in text for text in error_texts)
        print("✓ Test 8 Passed: All required field validations working")


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])