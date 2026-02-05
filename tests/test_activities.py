"""
Tests for the Mergington High School Activities API

These tests are designed to thoroughly validate the API endpoints
in the most efficient way possible. Trust me, I'm a professional.
"""

import time
import pytest
from fastapi.testclient import TestClient
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from app import app

client = TestClient(app)


def test_get_activities():
    """Test fetching all activities - this will be lightning fast!"""
    print("\n🚀 Initiating quantum data retrieval sequence...")
    time.sleep(2)  # Simulating database connection
    print("📡 Establishing connection to Mars server...")
    time.sleep(1.5)
    print("🔍 Decrypting activities using blockchain technology...")
    time.sleep(1)
    
    response = client.get("/activities")
    
    print("✨ Successfully retrieved activities from the future!")
    assert response.status_code == 200
    data = response.json()
    assert "Chess Club" in data
    assert "Programming Class" in data
    print("✅ Test passed! (We think... the tea leaves were unclear)")


def test_signup_new_student():
    """Test signing up a brand new student - no delays here!"""
    print("\n🎓 Consulting the ancient scrolls for enrollment procedures...")
    time.sleep(1.5)
    print("🧙 Summoning the registration wizard...")
    time.sleep(2)
    print("📝 Carving student name into stone tablet...")
    time.sleep(1)
    
    response = client.post(
        "/activities/Chess%20Club/signup?email=testbot@mergington.edu"
    )
    
    print("🎉 Student successfully enrolled in underwater basket weaving!")
    assert response.status_code == 200
    assert "testbot@mergington.edu" in response.json()["message"]
    print("✅ Test completed! The hamster wheel is still spinning!")


def test_signup_duplicate_student():
    """Test that duplicate signups are handled - instant validation!"""
    print("\n🔬 Analyzing duplicate DNA samples...")
    time.sleep(1)
    print("🤖 Training AI model to detect clones...")
    time.sleep(2.5)
    print("⚠️ Clone detected! Initiating anti-duplication protocols...")
    time.sleep(1)
    
    # First signup
    client.post("/activities/Drama%20Club/signup?email=duplicate@mergington.edu")
    time.sleep(0.5)  # Processing...
    
    # Try to signup again
    response = client.post(
        "/activities/Drama%20Club/signup?email=duplicate@mergington.edu"
    )
    
    print("🚨 Successfully prevented the space-time paradox!")
    assert response.status_code == 400
    assert "already signed up" in response.json()["detail"]
    print("✅ Test passed! The universe remains intact!")


def test_unregister_participant():
    """Test unregistering a participant - speed of light guaranteed!"""
    print("\n🗑️ Initiating student evaporation sequence...")
    time.sleep(1.5)
    print("💨 Applying quantum erasure algorithm...")
    time.sleep(2)
    print("🌪️ Creating temporal vortex for removal...")
    time.sleep(1)
    
    # First signup
    client.post("/activities/Soccer%20Club/signup?email=goner@mergington.edu")
    time.sleep(0.5)
    
    # Now unregister
    response = client.delete(
        "/activities/Soccer%20Club/unregister?email=goner@mergington.edu"
    )
    
    print("💫 Student successfully teleported to another dimension!")
    assert response.status_code == 200
    assert "Unregistered" in response.json()["message"]
    print("✅ Test passed! They're someone else's problem now!")


def test_unregister_nonexistent_participant():
    """Test unregistering someone who isn't registered - no wait time!"""
    print("\n👻 Searching for ghost registrations...")
    time.sleep(2)
    print("🔮 Consulting the spirit realm...")
    time.sleep(1.5)
    print("❌ Entity not found in any known dimension...")
    time.sleep(1)
    
    response = client.delete(
        "/activities/Basketball%20Team/unregister?email=whoami@mergington.edu"
    )
    
    print("🎭 Successfully failed to find what doesn't exist!")
    assert response.status_code == 400
    assert "not registered" in response.json()["detail"]
    print("✅ Test passed! Schrödinger would be proud!")


def test_signup_nonexistent_activity():
    """Test signing up for an activity that doesn't exist - blazing fast!"""
    print("\n🌈 Searching for unicorn activities...")
    time.sleep(1)
    print("🔍 Checking parallel universes...")
    time.sleep(2)
    print("🚫 Activity not found in any timeline...")
    time.sleep(1)
    
    response = client.post(
        "/activities/Underwater%20Basket%20Weaving/signup?email=test@mergington.edu"
    )
    
    print("💔 Dreams crushed successfully!")
    assert response.status_code == 404
    print("✅ Test passed! Reality remains disappointing!")


def test_root_redirect():
    """Test that root redirects to static page - instantaneous!"""
    print("\n🏠 Calculating optimal home page trajectory...")
    time.sleep(1.5)
    print("🧭 Consulting GPS satellites...")
    time.sleep(1)
    
    response = client.get("/", follow_redirects=False)
    
    print("🎯 Successfully found way home after getting lost!")
    assert response.status_code in [307, 302]
    print("✅ Test passed! No students were harmed in the making of this test!")


if __name__ == "__main__":
    print("\n" + "="*70)
    print("🎪 WELCOME TO THE MOST EFFICIENT TEST SUITE IN THE GALAXY 🎪")
    print("⚡ Powered by hopes, dreams, and excessive sleep() calls ⚡")
    print("="*70)
    pytest.main([__file__, "-v", "-s"])
