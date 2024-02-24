document.addEventListener('DOMContentLoaded', function () {
  const navItems = document.querySelectorAll('.nav-item');
  const tabContents = document.querySelectorAll('.tabcontent');
  navItems.forEach(item => {
    item.addEventListener('click', () => {
      const tabId = item.getAttribute('data-tab');
      activateTab(tabId);
    });
  });

  function activateTab(tabId) {
    navItems.forEach(item => {
      item.classList.remove('active');
    });

    tabContents.forEach(tabContent => {
      tabContent.classList.remove('active');
    });

    const selectedNavItem = document.querySelector(`.nav-item[data-tab="${tabId}"]`);
    const selectedTabContent = document.getElementById(tabId);
    selectedNavItem.classList.add('active');
    selectedTabContent.classList.add('active');
  }
  // Activate the first tab by default
  activateTab('choice1');
});

function startProcess() {
  const textarea = document.querySelector('.generate-code textarea');
  const generatedCode = document.getElementById('generatedCode');
  const generatedCodeDiv = document.querySelector('.generated-code');
  const generateCodeBtn = document.getElementById('generateCodeBtn');
  // Simulate code generation process (e.g., using entered text)
  const userInput = textarea.value;
  let generate_code_response = null;
  generateCodeBtn.innerHTML = "Generating code...";

  $.ajax({
    url: 'http://127.0.0.1:5000/generate-code',
    method: 'POST',
    data: JSON.stringify({ "prompt_str": userInput }),
    contentType: "application/json",
    async: false,
    beforeSend: function () {
      generateCodeBtn.innerHTML = "Generating code...";
    },
    success: function (response) {
      generate_code_response = response;
      console.log(generate_code_response)
      generateCodeBtn.innerHTML = "Start the process!";
    },
    error: function (xhr, status, error) {
      // Handle any errors
    }
  });
  const generatedText = generate_code_response
  // Display the generated code
  generatedCode.textContent = generatedText;
  generatedCodeDiv.style.display = 'block';
}

function startGeneratingData() {
  const fileInput = document.getElementById('csvFileInput');
  const textarea = document.getElementById('dataTextArea');
  const userInput = textarea.value;
  const file = fileInput.files[0];
  let generated_csv_response = null;
  if (file) {
    const reader = new FileReader();
    $.ajax({
      url: 'http://127.0.0.1:5000/augment-data',
      method: 'POST',
      data: JSON.stringify({ "prompt_str": userInput, "file_path": fileInput.files[0].name }),
      contentType: "application/json",
      async: false,
      success: function (response) {
        generated_csv_response = response;
        console.log(generated_csv_response)
      },
      error: function (xhr, status, error) {
        // Handle any errors
      }
    });

    reader.onload = function (event) {
      // const csvData = event.target.result;
      const csvData = generated_csv_response;
      const parsedData = parseCSV(csvData);
      // Display parsed CSV data in preview section
      displayPreview(parsedData);
    };

    reader.readAsText(file);
  } else {
    alert('Please select a CSV file.');
  }
}

function parseCSV(csvData) {
  // Dummy function to parse CSV data (replace with actual CSV parsing logic)
  const rows = csvData.split('\n');
  const data = [];
  for (let i = 0; i < Math.min(100, rows.length); i++) {
    const columns = rows[i].split(',');
    data.push(columns);
  }
  return data;
}

function displayPreview(data) {
  const previewTable = document.getElementById('previewTable');
  previewTable.innerHTML = '';
  for (let i = 0; i < data.length; i++) {
    const row = document.createElement('tr');
    for (let j = 0; j < data[i].length; j++) {
      const cell = document.createElement('td');
      cell.textContent = data[i][j];
      row.appendChild(cell);
    }
    previewTable.appendChild(row);
  }
  // Show the preview section
  document.querySelector('.file-preview').style.display = 'block';
}

function codeReview() {
  // const textarea = document.querySelector('.generate-code textarea');
  const generatedReview = document.getElementById('generatedReview');
  const generatedReviewDiv = document.querySelector('.generated-review');
  // const generateCodeBtn = document.getElementById('generateCodeBtn');
  // Simulate code generation process (e.g., using entered text)
  let generate_code_response = null;
  // generateCodeBtn.innerHTML = "Generating code review...";
  const fileInput = document.getElementById('pyFileInput1');
  const textarea = document.getElementById('dataTextArea');
  const userInput = textarea.value;
  const file = fileInput.files[0];
  if (file) {
    const reader = new FileReader();
    $.ajax({
      url: 'http://127.0.0.1:5000/code-review',
      method: 'POST',
      data: JSON.stringify({ "prompt_str": userInput, "file_path": fileInput.files[0].name }),
      contentType: "application/json",
      async: false,
      success: function (response) {
        generate_code_response = response;
        console.log(generate_code_response)
        // return generate_code_response
        // generateCodeBtn.innerHTML = "Start the process!";
      },
      error: function (xhr, status, error) {
        // Handle any errors
      }
    });
    reader.readAsText(file)
  }else {
    alert('Please select a python file.');
  }
  const generatedText = generate_code_response
  // Display the generated code
  generatedReview.textContent = generatedText;
  generatedReviewDiv.style.display = 'block';
}

function docGeneration() {
  // const textarea = document.querySelector('.generate-code textarea');
  const generatedDoc = document.getElementById('generatedDoc');
  const generatedDocDiv = document.querySelector('.generated-document');
  // const generateCodeBtn = document.getElementById('generateCodeBtn');

  // Simulate code generation process (e.g., using entered text)
  const fileInput = document.getElementById('pyFileInput');
  const textarea = document.getElementById('dataTextArea');
  const userInput = textarea.value;

  let generate_code_response = null;
  const file = fileInput.files[0];
  // generateCodeBtn.innerHTML = "Generating code...";

  if (file) {
    const reader = new FileReader();
    $.ajax({
      url: 'http://127.0.0.1:5000/doc-generation',
      method: 'POST',
      data: JSON.stringify({ "prompt_str": userInput, "file_path": fileInput.files[0].name }),
      contentType: "application/json",
      async: false,
      beforeSend: function () {
        generateCodeBtn.innerHTML = "Generating code...";
      },
      success: function (response) {
        generate_code_response = response
        console.log(generate_code_response)
        // return generate_code_response
        // generateCodeBtn.innerHTML = "Start the process!";
      },
      error: function (xhr, status, error) {
        // Handle any errors
      }
    });
    // reader.readAsText(file)
  }else {
    alert('Please select a python file.');
  }
  const generatedText = generate_code_response
  // Display the generated code
  generatedDoc.textContent = generatedText;
  generatedDocDiv.style.display = 'block';
}

function commitAndPush(){
  const fileInput = document.getElementById('multiFileInput');
  const repoText = document.getElementById('repoTextField').value;
  const filePathText = document.getElementById('filePathTextField').value;
  const branchName = document.getElementById('branchNameField').value;
  const commitText = document.getElementById('commitTextField').value;
  // const responseText = document.getElementById('')
  const generatedGitLink = document.getElementById('generatedGitLink');
  const generatedGitLinkDiv = document.querySelector('.generated-git-link');

  const files = fileInput.files;
  let file_names = [];
  for(let file in files){
    if (files.hasOwnProperty(file)){
        file_names.push(files[file].name);
    }
  }
  data_to_send = JSON.stringify({ 
    "files": file_names,
    "repo_path": repoText,
    "target_path": filePathText,
    "branch_name": branchName,
    "commit_message": commitText
  });
  let generate_code_response = null;

  if (files) {
    const reader = new FileReader();
    $.ajax({
      url: 'http://127.0.0.1:5000/commit-and-push',
      method: 'POST',
      data: data_to_send,
      contentType: "application/json",
      async: false,
      success: function (response) {
        generate_code_response = response
      },
      error: function (xhr, status, error) {
        // Handle any errors
      }
    });
  } else {
    alert('Please select atleast one file.');
  }
  // Display the generated code
  generatedGitLink.textContent = generate_code_response;
  generatedGitLinkDiv.style.display = 'block';
}