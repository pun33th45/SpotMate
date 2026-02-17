#!/usr/bin/env python3
"""
Quick test to verify SpotMate rebranding and QR code fix
"""

import sys
sys.path.insert(0, r'c:\Users\PYadav\OneDrive\Desktop\Park-Matrix.AI')

import io
import qrcode

def test_qr_code_generation():
    """Test that QR code generation and bytes conversion works"""
    print("🧪 Testing QR Code Generation...")
    
    # Generate QR code
    booking_id = "BK5001"
    location = "Hitech City"
    date = "2026-02-17"
    time = "14:30"
    
    qr_data = f"BookingID:{booking_id}|Location:{location}|Date:{date}|Time:{time}"
    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(qr_data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Convert to bytes (this was causing the error)
    img_bytes = io.BytesIO()
    img.save(img_bytes, format="PNG")
    img_bytes.seek(0)
    
    # Verify both exist
    assert img is not None, "PIL Image not created"
    assert img_bytes is not None, "BytesIO not created"
    assert len(img_bytes.getvalue()) > 0, "BytesIO is empty"
    
    print(f"✅ PIL Image created: {type(img)}")
    print(f"✅ BytesIO buffer created: {len(img_bytes.getvalue())} bytes")
    print(f"✅ QR code data: {qr_data}")
    
    return True

def test_app_imports():
    """Test that the app imports correctly"""
    print("\n🧪 Testing App Imports...")
    
    try:
        # Note: We're not running streamlit, just checking imports
        import pandas as pd
        import numpy as np
        import plotly.graph_objects as go
        
        print("✅ pandas imported")
        print("✅ numpy imported")
        print("✅ plotly imported")
        print("✅ qrcode imported")
        
        return True
    except Exception as e:
        print(f"❌ Import error: {e}")
        return False

def test_branding():
    """Quick check that branding is consistent"""
    print("\n🧪 Checking Rebranding...")
    
    # Read the app.py file with UTF-8 encoding
    with open(r'c:\Users\PYadav\OneDrive\Desktop\Park-Matrix.AI\app.py', 'r', encoding='utf-8') as f:
        content = f.read()
    
    checks = {
        "SpotMate in title": 'page_title="SpotMate' in content,
        "Green header color": '#6FBF9B' in content,
        "\"List Your Spot\"": '"📍 List Your Spot"' in content,
        "\"Smart Insights\"": '"💡 Smart Insights"' in content,
        "\"Entry Pass\"": '"📲 Entry Pass"' in content,
        "SpotMate header": '<h1>🅿️ SpotMate</h1>' in content,
        "QR code fix (img_bytes)": 'qr_img, qr_img_bytes = generate_qr_code' in content,
        "Display bytes": 'st.image(qr_img_bytes' in content,
    }
    
    for check_name, result in checks.items():
        status = "✅" if result else "❌"
        print(f"{status} {check_name}")
    
    all_passed = all(checks.values())
    return all_passed

if __name__ == "__main__":
    print("=" * 60)
    print("SpotMate MVP - Rebranding & QR Code Test")
    print("=" * 60)
    
    results = []
    
    # Run tests
    results.append(("QR Code Generation", test_qr_code_generation()))
    results.append(("App Imports", test_app_imports()))
    results.append(("Rebranding", test_branding()))
    
    # Summary
    print("\n" + "=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "✅ PASSED" if result else "❌ FAILED"
        print(f"{status}: {test_name}")
    
    print("\n" + "=" * 60)
    if passed == total:
        print(f"🎉 ALL TESTS PASSED ({passed}/{total})")
        print("🚀 Ready to run: streamlit run app.py")
    else:
        print(f"⚠️  ({passed}/{total}) tests passed")
    print("=" * 60)
