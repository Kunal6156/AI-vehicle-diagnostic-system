# Test Examples for Alto Car Digital Manual

This file contains sample queries and test cases to verify the system functionality.

## Text Query Test Cases

### 1. Warning Light Queries

**Test Case 1.1**: Engine Check Light
```
Query: "What does the engine check light mean in my Alto?"
Expected: Explanation of engine malfunction indicator, possible causes, action steps
```

**Test Case 1.2**: Oil Pressure Warning
```
Query: "My Alto shows a red oil can symbol, what should I do?"
Expected: Low oil pressure warning, immediate action needed, check oil level
```

**Test Case 1.3**: Battery Light
```
Query: "Battery warning light is on in my Alto 800"
Expected: Charging system issue, check alternator and battery, diagnostic steps
```

### 2. AC/Climate Control Issues

**Test Case 2.1**: AC Not Cooling
```
Query: "My Alto AC is not cooling properly"
Expected: Possible causes (low gas, compressor, condenser), troubleshooting steps
```

**Test Case 2.2**: AC Making Noise
```
Query: "Strange noise from AC when turned on in my Alto"
Expected: Belt issues, compressor bearing, blower motor problems
```

### 3. Starting Problems

**Test Case 3.1**: No Start Condition
```
Query: "Alto car not starting, only clicking sound"
Expected: Battery/starter motor issues, testing procedures, solutions
```

**Test Case 3.2**: Intermittent Starting
```
Query: "Sometimes my Alto starts, sometimes it doesn't"
Expected: Electrical connection issues, fuel pump, ignition switch problems
```

### 4. Brake Issues

**Test Case 4.1**: Squeaking Brakes
```
Query: "My Alto brakes are making squeaking noise"
Expected: Worn brake pads, dust buildup, when to replace
```

**Test Case 4.2**: Soft Brake Pedal
```
Query: "Brake pedal feels soft in my Alto K10"
Expected: Air in brake lines, brake fluid leak, master cylinder issues
```

### 5. Maintenance Questions

**Test Case 5.1**: Oil Change
```
Query: "How to change engine oil in Maruti Alto?"
Expected: Step-by-step process, oil type, frequency, tools needed
```

**Test Case 5.2**: Service Schedule
```
Query: "What is the service schedule for Alto 800?"
Expected: Service intervals, tasks at each service, maintenance checklist
```

### 6. Dashboard Controls

**Test Case 6.1**: Hazard Lights
```
Query: "How to use hazard lights in Alto?"
Expected: Location, function, when to use
```

**Test Case 6.2**: Defogger
```
Query: "What is the rear defogger button in Alto?"
Expected: Symbol, function, usage in rainy weather
```

---

## Image Analysis Test Scenarios

### Scenario 1: Dashboard Components

**Test Images to Upload**:
- Speedometer/odometer display
- Fuel gauge
- Temperature gauge
- RPM meter

**Expected Analysis**:
- Component identification
- Function description
- Normal vs abnormal readings
- Related issues

### Scenario 2: Warning Lights

**Test Images to Upload**:
- Check engine light (amber)
- Oil pressure light (red)
- Battery light (red)
- Brake warning light
- ABS light
- Airbag light

**Expected Analysis**:
- Light identification
- Color significance
- Meaning and urgency
- Immediate actions required
- Related video tutorials

### Scenario 3: Buttons and Controls

**Test Images to Upload**:
- AC button
- Hazard light button
- Power window switch
- Central locking button
- Defogger button

**Expected Analysis**:
- Button identification
- Symbol meaning
- Function explanation
- Usage instructions

### Scenario 4: Engine Components

**Test Images to Upload**:
- Engine oil dipstick
- Coolant reservoir
- Battery terminals
- Air filter
- Brake fluid reservoir

**Expected Analysis**:
- Component name
- Location in engine bay
- Checking procedure
- Maintenance tips

### Scenario 5: Under Car Components

**Test Images to Upload**:
- Brake discs/pads
- Tire condition
- Suspension parts
- Exhaust system

**Expected Analysis**:
- Wear assessment
- Replacement indicators
- Safety concerns

---

## Video Analysis Test Scenarios

### Scenario 1: Engine Running
**Test Video**: Record engine running
**Expected**: Sound analysis, smooth/rough running assessment

### Scenario 2: Dashboard While Driving
**Test Video**: Record dashboard during operation
**Expected**: Gauge readings, warning light detection

### Scenario 3: Strange Sounds
**Test Video**: Record unusual car noises
**Expected**: Sound identification, possible causes

---

## Error Handling Test Cases

### 1. Invalid Inputs

**Test Case 1.1**: Empty text query
```
Input: ""
Expected: Error message "Please enter a question"
```

**Test Case 1.2**: Very short query
```
Input: "AC"
Expected: Error message "Please provide more details"
```

**Test Case 1.3**: Invalid file type
```
Input: .txt or .doc file
Expected: Error message "Invalid file type"
```

**Test Case 1.4**: File too large
```
Input: 20MB image
Expected: Error message "File size must be less than 16MB"
```

### 2. API Failures

**Test Case 2.1**: Invalid Gemini API key
```
Setup: Wrong API key in .env
Expected: Error message about API configuration
```

**Test Case 2.2**: Invalid YouTube API key
```
Setup: Wrong YouTube key in .env
Expected: Videos section shows error or empty
```

**Test Case 2.3**: Network disconnected
```
Setup: Disable internet
Expected: Network error message
```

---

## Performance Test Cases

### 1. Response Time

**Test Case 1.1**: Image analysis
```
Metric: Time from upload to results
Target: < 5 seconds
```

**Test Case 1.2**: Text query
```
Metric: Time from submit to results
Target: < 3 seconds
```

**Test Case 1.3**: Video search
```
Metric: Time to load YouTube videos
Target: < 2 seconds
```

### 2. Concurrent Users

**Test Case 2.1**: Multiple simultaneous queries
```
Setup: 5 users analyzing simultaneously
Expected: All requests complete successfully
```

### 3. Large Files

**Test Case 3.1**: Maximum size image
```
Setup: Upload 15MB image
Expected: Processes successfully
```

---

## Integration Test Cases

### 1. End-to-End Workflows

**Workflow 1**: Complete image analysis flow
```
1. Navigate to home page
2. Click Image Analysis tab
3. Upload car image
4. Click Analyze
5. View AI analysis
6. Scroll to videos section
7. Click video link
8. Verify YouTube video opens
```

**Workflow 2**: Complete text query flow
```
1. Navigate to home page
2. Click Ask Question tab
3. Enter question
4. Click Get Answer
5. View detailed answer
6. Check video recommendations
7. Click on video
```

**Workflow 3**: Knowledge base navigation
```
1. Click Manual link in navbar
2. Scroll through sections
3. Verify all information displays
4. Click "Go to Analysis Tool" button
5. Verify redirect to home page
```

### 2. Cross-Tab Functionality

**Test Case 2.1**: Switch tabs
```
1. Start with image upload
2. Switch to text query tab
3. Switch to video tab
4. Verify all tabs work independently
```

**Test Case 2.2**: Multiple analyses
```
1. Analyze an image
2. Switch to text query
3. Ask a question
4. Verify both results are independent
```

---

## Browser Compatibility Tests

Test on:
- ✅ Chrome (latest)
- ✅ Firefox (latest)
- ✅ Safari (latest)
- ✅ Edge (latest)
- ✅ Mobile Chrome
- ✅ Mobile Safari

**Test Cases**:
- Page loading
- File upload
- Form submission
- Video display
- Responsive design

---

## Accessibility Tests

**Test Case 1**: Keyboard navigation
```
Use Tab key to navigate
All interactive elements accessible
```

**Test Case 2**: Screen reader compatibility
```
Test with NVDA or JAWS
All content readable
```

**Test Case 3**: Color contrast
```
Check text visibility
Verify WCAG compliance
```

---

## Security Tests

**Test Case 1**: File upload validation
```
Try uploading .exe, .php files
Expected: Rejected
```

**Test Case 2**: SQL injection (if using database)
```
Input: ' OR '1'='1
Expected: Sanitized, no effect
```

**Test Case 3**: XSS attempts
```
Input: <script>alert('test')</script>
Expected: Escaped, not executed
```

---

## Sample Test Results Format

```
Test Date: YYYY-MM-DD
Test Environment: Local / Production
Tester: [Name]

Test Case ID: 1.1
Test Case: Engine Check Light Query
Status: ✅ PASS / ❌ FAIL
Response Time: 2.3 seconds
Notes: Analysis accurate, 5 relevant videos returned

Test Case ID: 1.2
Test Case: Image Upload - Warning Light
Status: ✅ PASS
Response Time: 4.1 seconds
Notes: Correctly identified brake warning light
```

---

## Automated Testing (Future Enhancement)

### Unit Tests
```python
# Test Gemini service
def test_gemini_image_analysis():
    result = gemini_service.analyze_image(test_image_path)
    assert result['success'] == True
    assert 'analysis' in result

# Test YouTube service
def test_youtube_search():
    result = youtube_service.search_videos("Alto repair")
    assert result['success'] == True
    assert len(result['videos']) > 0
```

### Integration Tests
```python
# Test API endpoint
def test_analyze_endpoint():
    response = client.post('/analyze', data={
        'type': 'text',
        'query': 'Test query'
    })
    assert response.status_code == 200
    assert 'analysis' in response.json
```

---

## Pre-Deployment Checklist

Before DRDO presentation:

- [ ] All API keys configured
- [ ] Test image analysis with 5 different images
- [ ] Test text queries with 10 different questions
- [ ] Verify video search returns relevant results
- [ ] Check manual page displays correctly
- [ ] Test on mobile device
- [ ] Verify error handling
- [ ] Check response times
- [ ] Prepare backup demo (screenshots/video)
- [ ] Test internet connectivity
- [ ] Have sample images ready
- [ ] Review presentation points

---

## Known Limitations

1. **Video Analysis**: Currently simplified (frame extraction not fully implemented)
2. **API Quota**: Limited to free tier quotas
3. **No User Authentication**: Single-user system
4. **No History**: Previous analyses not saved
5. **Local Storage**: Files stored locally (not cloud)

---

## Success Criteria

✅ System responds within 5 seconds  
✅ AI provides relevant analysis 85%+ of time  
✅ YouTube videos are relevant (4+/5 rating)  
✅ No crashes or critical errors  
✅ Works on different browsers  
✅ Mobile responsive  
✅ Professional UI/UX  

---

**Testing Status**: Ready for comprehensive testing
**Last Updated**: 2024
**Next Review**: Before DRDO presentation
