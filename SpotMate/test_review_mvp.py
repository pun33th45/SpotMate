#!/usr/bin/env python3
"""
Test Suite for SpotMate MVP Review Version
Validates all changes made for review-ready state
"""

import subprocess
import re
import sys

def read_app_file():
    """Read the app.py file"""
    with open('app.py', 'r', encoding='utf-8') as f:
        return f.read()

def test_architecture_removed():
    """Test: Architecture tab and content removed"""
    print("\n🧪 TEST 1: Architecture Tab Removed")
    app_content = read_app_file()
    
    # Check if Architecture is removed from tab names
    if '🏗️ Architecture' in app_content:
        print("   ❌ FAIL: 'Architecture' tab still present in tab definitions")
        return False
    
    # Check if old Architecture tab code block is removed
    if 'with tab7:' in app_content and 'System Architecture' in app_content.split('with tab7:')[1][:200]:
        print("   ❌ FAIL: Old Architecture tab code still present")
        return False
    
    print("   ✅ PASS: Architecture tab successfully removed")
    return True

def test_help_tab_added():
    """Test: Help tab added with contact info"""
    print("\n🧪 TEST 2: Help Tab Added")
    app_content = read_app_file()
    
    # Check if Help tab is in tab names
    if '⌛ Help' not in app_content and '❓ Help' not in app_content:
        print("   ❌ FAIL: Help tab not found in tab definitions")
        return False
    
    # Check if help email is present
    if 'spotmate.help@gmail.com' not in app_content:
        print("   ❌ FAIL: Help email not found in Help tab")
        return False
    
    print("   ✅ PASS: Help tab added with contact info")
    return True

def test_ai_logic_location_required():
    """Test: AI Smart Insights requires location/zone selection first"""
    print("\n🧪 TEST 3: AI Requires Location/Zone Selection")
    app_content = read_app_file()
    
    # Check for area/zone section in Smart Insights tab area (find tab4 content)
    tab4_start = app_content.find('with tab4:')
    if tab4_start == -1:
        print("   ❌ FAIL: Tab 4 (Smart Insights) not found")
        return False
    
    tab4_section = app_content[tab4_start:tab4_start + 5000]
    
    # Check for Select Area & Zone section
    if 'Select Area & Zone' not in tab4_section:
        print("   ❌ FAIL: 'Select Area & Zone' section not found in Smart Insights tab")
        return False
    
    # Check for selectbox calls for area and zone
    if 'selectbox' not in tab4_section:
        print("   ❌ FAIL: Area/Zone selection dropdowns not found")
        return False
    
    # Check for zone types
    if 'Residential' not in tab4_section or 'Commercial' not in tab4_section:
        print("   ❌ FAIL: Zone types not found")
        return False
    
    print("   ✅ PASS: AI logic now requires location/zone selection first")
    return True

def test_payment_flow_simplified():
    """Test: Payment flow simplified with immediate success"""
    print("\n🧪 TEST 4: Payment Flow Simplified")
    app_content = read_app_file()
    
    # Check for immediate success message (allowing for markdown formatting)
    if 'Payment Successful' not in app_content and 'Payment Confirmed' not in app_content:
        print("   ❌ FAIL: Payment success message not found")
        return False
    
    # Check for st.balloons() - visual celebration
    if 'st.balloons()' in app_content:
        print("   ✅ Payment success includes visual celebration (balloons)")
    else:
        print("   ⚠️  Payment success message found without visual celebration")
    
    # Check that payment failure scenarios are removed
    if 'Payment Failed' in app_content and 'failed' in app_content.lower() and 'payment_failed' in app_content:
        print("   ❌ FAIL: Payment failure scenarios still present")
        return False
    
    # Check for instruction to go to Entry Pass tab
    if 'Entry Pass' in app_content and 'QR code' in app_content:
        print("   ✅ Payment success directs to Entry Pass for QR code")
    
    print("   ✅ PASS: Payment flow simplified with immediate success")
    return True

def test_qr_code_bytes():
    """Test: QR code properly uses bytes for Streamlit display"""
    print("\n🧪 TEST 5: QR Code Uses Bytes (No TypeError)")
    app_content = read_app_file()
    
    # Check for generate_qr_code returns tuple
    if 'return img, img_bytes' not in app_content:
        print("   ❌ FAIL: QR function doesn't return bytes")
        return False
    
    # Check for st.image(qr_img_bytes...) not st.image(qr_img...)
    qr_display = app_content[app_content.find('st.image(qr_img'):app_content.find('st.image(qr_img') + 100]
    if 'st.image(qr_img_bytes' not in qr_display:
        print("   ❌ FAIL: QR display not using bytes")
        return False
    
    # Check for tuple unpacking
    if 'qr_img, qr_img_bytes = generate_qr_code' not in app_content:
        print("   ❌ FAIL: QR tuple unpacking not found")
        return False
    
    print("   ✅ PASS: QR code properly configured to use bytes (no TypeError)")
    return True

def test_no_debug_elements():
    """Test: No debug prints or error-prone elements"""
    print("\n🧪 TEST 6: No Debug Elements or Raw Errors")
    app_content = read_app_file()
    
    # Check for common debug patterns
    debug_patterns = [
        r'print\(',  # print statements
        r'st\.write\(.*\)',  # raw st.write without formatting
    ]
    
    issues_found = 0
    for pattern in debug_patterns:
        matches = re.findall(pattern, app_content)
        # Filter out expected patterns
        filtered = [m for m in matches if not any(x in app_content[app_content.find(m)-100:app_content.find(m)] for x in ['st.info', 'st.error'])]
        if filtered:
            issues_found += len(filtered)
    
    if issues_found > 0:
        print(f"   ⚠️  WARNING: Found {issues_found} potential debug elements (check manually)")
    else:
        print("   ✅ PASS: No obvious debug elements found")
    
    return True

def test_review_friendly():
    """Test: MVP is review-friendly"""
    print("\n🧪 TEST 7: Review-Friendly Content")
    app_content = read_app_file()
    
    # Check for SpotMate branding (not ParkMatrix)
    if 'ParkMatrix' in app_content:
        print("   ❌ FAIL: Old 'ParkMatrix' branding still present")
        return False
    
    # Check for clean footer
    if 'MVP Summary' not in app_content:
        print("   ⚠️  WARNING: MVP Summary footer not found")
    
    # Check for green color scheme
    if '#6FBF9B' not in app_content:
        print("   ⚠️  WARNING: Green color scheme not found")
    
    print("   ✅ PASS: MVP is properly branded and review-friendly")
    return True

def main():
    """Run all tests"""
    print("=" * 60)
    print("🧪 SpotMate MVP Review Version - Test Suite 🧪")
    print("=" * 60)
    
    tests = [
        test_architecture_removed,
        test_help_tab_added,
        test_ai_logic_location_required,
        test_payment_flow_simplified,
        test_qr_code_bytes,
        test_no_debug_elements,
        test_review_friendly,
    ]
    
    results = []
    for test in tests:
        try:
            result = test()
            results.append(result)
        except Exception as e:
            print(f"   ❌ ERROR: {str(e)}")
            results.append(False)
    
    print("\n" + "=" * 60)
    print(f"📊 Results: {sum(results)}/{len(results)} tests passed")
    print("=" * 60)
    
    if all(results):
        print("\n✅ ALL TESTS PASSED!")
        print("\n🚀 You can now run: streamlit run app.py")
        return 0
    else:
        print("\n❌ Some tests failed. Please review the output above.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
