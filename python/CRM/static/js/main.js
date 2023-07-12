const ctx = document.getElementById('revenueChart');

// const chartLabels = document.querySelectorAll('.chartLabel');
// const chartValues = document.querySelectorAll('.chartValue');

// const chartlabelArr = [];
// const chartValueArr = [];

// chartLabels.forEach((label) => chartlabelArr.push(label.innerText));
// chartValues.forEach((value) => chartValueArr.push(value.innerText));

function revenueChart() {
  new Chart(ctx, {
    type: 'bar',
    data: {
      labels: labels,
      datasets: [
        {
          label: 'Monthly Revenue of 2023',
          data: revenues,
          borderWidth: 1,
        },
      ],
    },
    options: {
      scales: {
        y: {
          beginAtZero: true,
        },
      },
    },
  });
}

revenueChart();
