<template>
  <div class="py-12 bg-white">
    <div>
      <div class="text-center">

        <p
          class=" text-3xl leading-8 font-extrabold tracking-tight text-gray-900"
        >
          Machine learning models we used
        </p>
        <p class="mt-4 max-w-2xl text-xl text-gray-500 mx-auto">
          In this project, four machine learning models will be applied to build
          a more reliable and accurate phishing detection tool.
        </p>
      </div>
      <div class="mt-20">
        <dl
          class="space-y-0 grid grid-cols-2 gap-x-5 gap-y-10"
        >
          <div class="relative">
            <dt>
              <div
                class="absolute flex items-center justify-center h-12 w-12 rounded-md bg-indigo-500 text-white"
              >
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
                    d="M8.684 13.342C8.886 12.938 9 12.482 9 12c0-.482-.114-.938-.316-1.342m0 2.684a3 3 0 110-2.684m0 2.684l6.632 3.316m-6.632-6l6.632-3.316m0 0a3 3 0 105.367-2.684 3 3 0 00-5.367 2.684zm0 9.316a3 3 0 105.368 2.684 3 3 0 00-5.368-2.684z"
                  />
                </svg>
              </div>
              <p class="ml-16 text-lg leading-6 font-medium text-gray-900">
                Decision Tree Model
              </p>
            </dt>
            <dd class="mt-2 ml-16 text-base text-gray-500">
              Used to partitions the data keep into subsets with a binary split
              until no split can be made by forming variable breaches
            </dd>
          </div>

          <div class="relative">
            <dt>
              <div
                class="absolute flex items-center justify-center h-12 w-12 rounded-md bg-indigo-500 text-white"
              >
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
                    d="M13 17h8m0 0V9m0 8l-8-8-4 4-6-6"
                  />
                </svg>
              </div>
              <p class="ml-16 text-lg leading-6 font-medium text-gray-900">
                Support Vector Machine(SVM) Model
              </p>
            </dt>
            <dd class="mt-2 ml-16 text-base text-gray-500">
              Used to analyze data for classification and regression analysis to
              find hyperplane in an N-dimensional space that distinctly
              classifies the data points with less computation power.
            </dd>
          </div>

          <div class="relative">
            <dt>
              <div
                class="absolute flex items-center justify-center h-12 w-12 rounded-md bg-indigo-500 text-white"
              >
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
                    d="M13 10V3L4 14h7v7l9-11h-7z"
                  />
                </svg>
              </div>
              <p class="ml-16 text-lg leading-6 font-medium text-gray-900">
                Extreme Gradient Boosting(XGBoost) Model
              </p>
            </dt>
            <dd class="mt-2 ml-16 text-base text-gray-500">
              An implementation of gradient boosted decision trees designed for
              speed and performance for structured or tabular data, used on a
              large number of data problem based on providing a parallel tree
              boosting.
            </dd>
          </div>

          <div class="relative">
            <dt>
              <div
                class="absolute flex items-center justify-center h-12 w-12 rounded-md bg-indigo-500 text-white"
              >
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
                    d="M12 6V4m0 2a2 2 0 100 4m0-4a2 2 0 110 4m-6 8a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4m6 6v10m6-2a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4"
                  />
                </svg>
              </div>
              <p class="ml-16 text-lg leading-6 font-medium text-gray-900">
                Multilayer Perceptron(Deep Learning) Model
              </p>
            </dt>
            <dd class="mt-2 ml-16 text-base text-gray-500">
              Uses a linear activation function to utilizes a supervised
              learning technique for data training, usually applied in-process
              data with regression structures.
            </dd>
          </div>
        </dl>
      </div>
      <!-- <div class="mt-10 text-center">
        <div class="inline-flex rounded-md shadow">
        <a href="#" class="inline-flex items-center justify-center px-5 py-3 border border-transparent text-base font-medium rounded-md text-white bg-indigo-500 hover:bg-indigo-700">
          Get started
        </a>
      </div>
      </div> -->
    </div>
  </div>
</template>