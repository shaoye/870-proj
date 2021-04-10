<template>
  <!-- This example requires Tailwind CSS v2.0+ -->
  <div>
    <nav class="bg-gray-800">
      <div class="max-w-7xl mx-auto px-4">
        <div class="flex items-center justify-between h-16">
          <div class="flex items-center">
            <div class="flex-shrink-0">
              <img
                class="h-8 w-8"
                src="https://tailwindui.com/img/logos/workflow-mark-indigo-500.svg"
                alt="Workflow"
              />
            </div>
            <div class="hidden md:block">
              <div class="ml-10 flex items-baseline space-x-4">
                <!-- Current: "bg-gray-900 text-white", Default: "text-gray-300 hover:bg-gray-700 hover:text-white" -->
                <a
                  href="#"
                  @click="navigate('Dashboard')"
                  v-bind:class="[
                    pageName === 'Dashboard' ? activeStyle : defaultStyle,
                  ]"
                  >Dashboard</a
                >

                <a
                  href="#"
                  @click="navigate('Models')"
                  v-bind:class="[
                    pageName === 'Models' ? activeStyle : defaultStyle,
                  ]"
                  >Models</a
                >

                <a
                  href="#"
                  @click="navigate('Reports')"
                  v-bind:class="[
                    pageName === 'Reports' ? activeStyle : defaultStyle,
                  ]"
                  >Reports</a
                >
              </div>
            </div>
          </div>
          <div class="hidden md:block">
            <div class="ml-4 flex items-center">
              <button
                class="bg-gray-800 p-1 rounded-full text-gray-400 hover:text-white focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-offset-gray-800 focus:ring-white"
              >
                <span class="sr-only">View notifications</span>
                <!-- Heroicon name: outline/bell -->
                <svg
                  class="h-6 w-6"
                  xmlns="http://www.w3.org/2000/svg"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                  aria-hidden="true"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9"
                  />
                </svg>
              </button>
            </div>
          </div>
        </div>
      </div>
    </nav>

    <header class="bg-white shadow">
      <div class="max-w-7xl mx-auto py-6 px-4 sm:px-6 lg:px-8">
        <h1 class="text-3xl font-bold text-gray-900">
          {{ pageName }}
        </h1>
      </div>
    </header>
    <main>
      <div class="max-w-7xl mx-auto py-6 px-8">
        <div v-if="pageName === 'Dashboard'">
          <div class="bg-white">
            <div
              class="max-w-7xl mx-auto py-12 px-4 sm:px-6 lg:py-16 lg:px-8 lg:flex lg:items-center lg:justify-between"
            >
              <h2
                class="text-3xl font-extrabold tracking-tight text-gray-900 sm:text-4xl"
              >
                <span class="block">Phishing Detecter</span>
                <span class="block text-indigo-600"
                  >Just input the URL below</span
                >
              </h2>
              <div class="mt-8 flex lg:mt-0 lg:flex-shrink-0">
                <div class="inline-flex rounded-md shadow">
                  <a
                    href="#"
                    @click="check"
                    class="inline-flex items-center justify-center px-5 py-3 border border-transparent text-base font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700"
                  >
                    <svg v-if="checking"
                      class="animate-spin -ml-1 mr-3 h-5 w-5 text-white"
                      xmlns="http://www.w3.org/2000/svg"
                      fill="none"
                      viewBox="0 0 24 24"
                    >
                      <circle
                        class="opacity-25"
                        cx="12"
                        cy="12"
                        r="10"
                        stroke="currentColor"
                        stroke-width="4"
                      ></circle>
                      <path
                        class="opacity-75"
                        fill="currentColor"
                        d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
                      ></path>
                    </svg>
                    Detect It!
                  </a>
                </div>
              </div>
            </div>
            <input
              class="shadow-lg appearance-none border rounded w-full h-16 p-3 text-gray-700 leading-tight focus:ring transform transition hover:scale-105 duration-300 ease-in-out"
              type="text"
              v-model="inputUrl"
              placeholder="https://some.phishing.url.com"
            />
          </div>
        </div>

        <model v-if="pageName === 'Models'"></model>

        <reports v-if="pageName === 'Reports'" :data="reportData" :url="inputUrl"></reports>
      </div>
    </main>
  </div>
</template>

<script>
import Model from "./components/Model.vue"
import Reports from "./components/Reports.vue"

export default {
  name: "HelloWorld",
  components: {
    Model,
    Reports
  },
  data() {
    return {
      inputUrl: "",
      pageName: "Dashboard",
      activeStyle: "bg-gray-900 text-white px-3 py-2 rounded-md text-sm font-medium",
      defaultStyle: "text-gray-300 hover:bg-gray-700 hover:text-white px-3 py-2 rounded-md text-sm font-medium",
      checkUrl: "http://localhost:5000/check",
      reportData: null,
      checking: false
    };
  },
  methods: {
  navigate(name) {
    console.log(name)
    this.pageName = name;
  },
  check() {
    if (this.inputUrl.length == 0) return;
    this.checking = true
    let that = this
    this.axios.post(this.checkUrl, { url: this.inputUrl }).then((res) => {
      that.reportData = JSON.parse(res.data)
      this.checking = false
      that.pageName = "Reports"
    });
  },
}
};
</script>
<style>
</style>