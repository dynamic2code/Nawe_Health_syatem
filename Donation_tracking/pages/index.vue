<template>
    <div class="min-h-screen flex">
      <!-- Vertical Navigation Bar -->
      <nav class="w-1/5 bg-gray-800 text-white p-4">
        <ul class="space-y-4">
          <li><router-link to="/installation" class="block py-2 px-4 rounded hover:bg-gray-700">Installation</router-link></li>
          <li><router-link to="/mainApp" class="block py-2 px-4 rounded hover:bg-gray-700">Main App</router-link></li>
          <li><router-link to="/djangoDocumentation" class="block py-2 px-4 rounded hover:bg-gray-700">Django Documentation</router-link></li>
          <li><router-link to="/nuxtDocumentation" class="block py-2 px-4 rounded hover:bg-gray-700">Nuxt Documentation</router-link></li>
          <li><router-link to="/systemDiagrams" class="block py-2 px-4 rounded hover:bg-gray-700">System Diagrams</router-link></li>
        </ul>
      </nav>
  
      <!-- Main Content -->
      <div class="w-4/5 bg-gray-100 p-8">
        <div class="max-w-3xl mx-auto bg-white shadow-md rounded-lg p-6">
          <h1 class="text-4xl font-bold text-center mb-6">🌟 Announcing Our Open-Source Donation Tracking System Project! 🌟</h1>
          <p class="text-lg mb-4">Hello everyone!</p>
          <p class="text-lg mb-4">
            I'm excited to share a new open-source project I'm working on: a <strong>Donation Tracking System</strong> designed to help organizations manage donations efficiently and transparently. This project aims to make a positive impact, and I'm inviting you to join me on this journey! 🚀
          </p>
  
          <h2 class="text-2xl font-semibold mt-6 mb-4">Project Overview</h2>
          <ul class="list-disc list-inside mb-4">
            <li>Allow organizations to log and track donations.</li>
            <li>Provide detailed reporting and analytics.</li>
            <li>Offer a user-friendly interface for both donors and administrators.</li>
            <li>Ensure transparency and accountability in donation management.</li>
          </ul>
  
          <h2 class="text-2xl font-semibold mt-6 mb-4">Milestones and Roadmap</h2>
          <p class="text-lg mb-4">Here’s a glimpse into our project roadmap and key milestones:</p>
  
          <div class="mb-6">
            <h3 class="text-xl font-bold mb-2">1. Project Initialization (Month 1-2)</h3>
            <ul class="list-disc list-inside mb-2">
              <li>Define project objectives and scope.</li>
              <li>Choose the technology stack.</li>
              <li>Set up the project repository on GitHub.</li>
              <li>Write a detailed README file.</li>
              <li>Create an initial project roadmap.</li>
            </ul>
          </div>
  
          <div class="mb-6">
            <h3 class="text-xl font-bold mb-2">2. Basic Functionality Prototype (Month 3-4)</h3>
            <ul class="list-disc list-inside mb-2">
              <li>Implement user registration and login.</li>
              <li>Develop donation logging functionality.</li>
              <li>Create basic reporting (e.g., total donations received).</li>
              <li>Design a simple user interface.</li>
              <li>Set up a development environment guide for contributors.</li>
            </ul>
          </div>
  
          <div class="mb-6">
            <h3 class="text-xl font-bold mb-2">3. Alpha Release (Month 5)</h3>
            <ul class="list-disc list-inside mb-2">
              <li>Test core features for bugs and usability.</li>
              <li>Create documentation for setting up and using the system.</li>
              <li>Announce the alpha release on our channels.</li>
              <li>Invite feedback from early users and contributors.</li>
            </ul>
          </div>
  
          <div class="mb-6">
            <h3 class="text-xl font-bold mb-2">4. Expert Collaboration (Month 6)</h3>
            <ul class="list-disc list-inside mb-2">
              <li>Reach out to potential experts in healthcare and other relevant fields.</li>
              <li>Conduct meetings to gather their input.</li>
              <li>Incorporate expert feedback into the project roadmap.</li>
            </ul>
          </div>
  
          <div class="mb-6">
            <h3 class="text-xl font-bold mb-2">5. Feature Expansion (Month 7-8)</h3>
            <ul class="list-disc list-inside mb-2">
              <li>Implement advanced reporting and analytics.</li>
              <li>Develop donation tracking for different categories (e.g., funds, goods, services).</li>
              <li>Add multi-user roles and permissions (e.g., admin, donor, beneficiary).</li>
              <li>Enhance the user interface and experience.</li>
            </ul>
          </div>
  
          <div class="mb-6">
            <h3 class="text-xl font-bold mb-2">6. Beta Release (Month 9)</h3>
            <ul class="list-disc list-inside mb-2">
              <li>Perform extensive testing and bug fixing.</li>
              <li>Update documentation with new features.</li>
              <li>Announce the beta release and encourage more users to test and provide feedback.</li>
              <li>Conduct a beta testing period to gather more data.</li>
            </ul>
          </div>
  
          <div class="mb-6">
            <h3 class="text-xl font-bold mb-2">7. Community Building (Month 10)</h3>
            <ul class="list-disc list-inside mb-2">
              <li>Host webinars or live streams to showcase the project.</li>
              <li>Create a contributor guide and code of conduct.</li>
              <li>Actively engage with the community on social media and forums.</li>
              <li>Organize virtual or in-person meetups for contributors.</li>
            </ul>
          </div>
  
          <div class="mb-6">
            <h3 class="text-xl font-bold mb-2">8. Full Launch (Month 11)</h3>
            <ul class="list-disc list-inside mb-2">
              <li>Finalize all features and perform final testing.</li>
              <li>Prepare comprehensive user and developer documentation.</li>
              <li>Announce the official launch on all channels.</li>
              <li>Monitor the launch and address any immediate issues.</li>
            </ul>
          </div>
  
          <div class="mb-6">
            <h3 class="text-xl font-bold mb-2">9. Post-Launch Support and Updates (Month 12 and Beyond)</h3>
            <ul class="list-disc list-inside mb-2">
              <li>Set up a system for ongoing support and issue tracking.</li>
              <li>Plan regular updates and feature enhancements.</li>
              <li>Encourage continued community engagement and contributions.</li>
              <li>Gather long-term feedback and incorporate it into future versions.</li>
            </ul>
          </div>
  
          <div class="mb-6">
            <h3 class="text-xl font-bold mb-2">10. Partnerships and Integrations (Ongoing)</h3>
            <ul class="list-disc list-inside mb-2">
              <li>Identify and reach out to potential partners (e.g., NGOs, other tech projects).</li>
              <li>Develop integrations with other systems and platforms.</li>
              <li>Promote the project through partner channels.</li>
            </ul>
          </div>
  
          <h2 class="text-2xl font-semibold mt-6 mb-4">How You Can Get Involved</h2>
          <p class="text-lg mb-4">
            We need your expertise and passion to make this project a success! Whether you're a developer, designer, healthcare professional, or someone passionate about transparency and accountability, there's a place for you here.
          </p>
          <ul class="list-disc list-inside mb-4">
            <li><strong>Developers:</strong> Help us build and improve the system.</li>
            <li><strong>Designers:</strong> Create a user-friendly interface.</li>
            <li><strong>Healthcare Professionals:</strong> Provide insights to ensure the system meets real-world needs.</li>
            <li><strong>Everyone:</strong> Test the system, give feedback, and spread the word!</li>
          </ul>
  
          <h2 class="text-2xl font-semibold mt-6 mb-4">Join Us!</h2>
          <p class="text-lg mb-4">
            Follow our progress on <a href="https://github.com/dynamic2code/Donation_tracking" class="text-blue-500 underline">GitHub Django</a> or <a href="https://github.com/dynamic2code/Donation-_tracking" class="text-blue-500 underline">GitHub Nuxt</a>, where you can find all the details and how to contribute. Stay updated with our latest news and milestones. We can't wait to build something great together! 🎉
          </p>
        </div>
      </div>
    </div>
  </template>
  
  <script>

  </script>
  
  <style>
  /* Custom styles (if needed) */
  </style>
  
  