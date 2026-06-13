// ── File Upload Handling ───────────────────────────────────────
const resumeInput = document.getElementById('resumeInput');
const dropZone    = document.getElementById('dropZone');
const fileNameEl  = document.getElementById('fileName');

resumeInput.addEventListener('change', () => {
  if (resumeInput.files[0]) {
    fileNameEl.textContent = '✅ ' + resumeInput.files[0].name;
  }
});

dropZone.addEventListener('dragover', (e) => {
  e.preventDefault();
  dropZone.style.borderColor = '#6366f1';
});

dropZone.addEventListener('dragleave', () => {
  dropZone.style.borderColor = '';
});

dropZone.addEventListener('drop', (e) => {
  e.preventDefault();
  dropZone.style.borderColor = '';
  const file = e.dataTransfer.files[0];
  if (file && file.name.endsWith('.pdf')) {
    resumeInput.files = e.dataTransfer.files;
    fileNameEl.textContent = '✅ ' + file.name;
  } else {
    alert('Please upload a PDF file only.');
  }
});


// ── Main Analyze Function ──────────────────────────────────────
async function analyzeResume() {
  const file = resumeInput.files[0];
  const jobDesc = document.getElementById('jobDescription').value;

  if (!file) {
    alert('Please upload a PDF resume first.');
    return;
  }

  // Show loader
  document.getElementById('loader').classList.add('active');
  document.getElementById('uploadSection').style.display = 'none';

  const formData = new FormData();
  formData.append('resume', file);
  formData.append('job_description', jobDesc);

  try {
    const response = await fetch('/analyze', {
      method: 'POST',
      body: formData
    });

    const data = await response.json();

    if (data.error) {
      alert('Error: ' + data.error);
      resetAnalyzer();
      return;
    }

    renderResults(data);

  } catch (err) {
    alert('Something went wrong. Please try again.');
    console.error(err);
    resetAnalyzer();
  } finally {
    document.getElementById('loader').classList.remove('active');
  }
}


// ── Render Results ─────────────────────────────────────────────
function renderResults(data) {
  document.getElementById('resultsSection').style.display = 'block';

  // ATS Score Circle
  const atsScore = data.ats_score;
  document.getElementById('atsScore').textContent = atsScore;
  document.getElementById('atsLevel').textContent  = data.ats_level;
  animateCircle('atsFill', atsScore);

  // Job Match Circle
  const matchScore = data.job_match_percent;
  document.getElementById('matchScore').textContent = matchScore + '%';
  if (matchScore === 0) {
    document.getElementById('matchLevel').textContent = 'No JD provided';
  } else if (matchScore >= 60) {
    document.getElementById('matchLevel').textContent = 'Strong Match';
  } else if (matchScore >= 35) {
    document.getElementById('matchLevel').textContent = 'Moderate Match';
  } else {
    document.getElementById('matchLevel').textContent = 'Low Match';
  }
  animateCircle('matchFill', matchScore);

  // Total skills
  document.getElementById('totalSkills').textContent = data.total_skills_count;

  // Skills Grid
  const skillsGrid = document.getElementById('skillsGrid');
  skillsGrid.innerHTML = '';
  if (Object.keys(data.skills_found).length === 0) {
    skillsGrid.innerHTML = '<p style="color:var(--muted)">No recognizable skills found. Ensure your resume is text-based (not scanned).</p>';
  } else {
    for (const [category, skills] of Object.entries(data.skills_found)) {
      const div = document.createElement('div');
      div.className = 'skill-category';
      div.innerHTML = `
        <div class="category-name">${category}</div>
        <div class="skill-tags">
          ${skills.map(s => `<span class="skill-tag">${s}</span>`).join('')}
        </div>`;
      skillsGrid.appendChild(div);
    }
  }

  // Skill Gaps
  const gapsGrid = document.getElementById('gapsGrid');
  gapsGrid.innerHTML = data.skill_gaps
    .map(g => `<span class="gap-tag">Missing: ${g}</span>`).join('');

  // Matched Keywords
  if (data.matched_keywords && data.matched_keywords.length > 0) {
    document.getElementById('keywordsBlock').style.display = 'block';
    document.getElementById('keywordsGrid').innerHTML = data.matched_keywords
      .map(k => `<span class="keyword-tag">${k}</span>`).join('');
  }

  // Suggestions
  const suggList = document.getElementById('suggestionsList');
  suggList.innerHTML = data.suggestions
    .map(s => `<li>${s}</li>`).join('');

  // Contact Info
  document.getElementById('emailFound').textContent = data.contact_info.email;
  document.getElementById('phoneFound').textContent = data.contact_info.phone;

  // Scroll to results
  document.getElementById('resultsSection').scrollIntoView({ behavior: 'smooth' });
}


// ── Animate SVG Circle ─────────────────────────────────────────
function animateCircle(fillId, percent) {
  const circumference = 314;
  const offset = circumference - (percent / 100) * circumference;
  setTimeout(() => {
    document.getElementById(fillId).style.strokeDashoffset = offset;
  }, 200);
}


// ── Reset ──────────────────────────────────────────────────────
function resetAnalyzer() {
  document.getElementById('resultsSection').style.display  = 'none';
  document.getElementById('uploadSection').style.display   = 'block';
  document.getElementById('keywordsBlock').style.display   = 'none';
  document.getElementById('loader').classList.remove('active');
  resumeInput.value = '';
  fileNameEl.textContent = 'No file selected';
  document.getElementById('jobDescription').value = '';
  document.getElementById('atsFill').style.strokeDashoffset  = 314;
  document.getElementById('matchFill').style.strokeDashoffset = 314;
  window.scrollTo({ top: 0, behavior: 'smooth' });
}
