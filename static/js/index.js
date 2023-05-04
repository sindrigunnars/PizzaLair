document.addEventListener('DOMContentLoaded', () => {
  const openDetailsButtons = document.querySelectorAll('[data-details-target]')
  const closeDetailsButtons = document.querySelectorAll('[data-close-button]')
  const overlay = document.getElementById('overlay')

  openDetailsButtons.forEach(button => {
      button.addEventListener('click', () => {
          const details = document.querySelector(button.dataset.detailsTarget)
          openDetails(details)
      })
  })

  overlay.addEventListener('click', () => {
      const details = document.querySelectorAll('.details.active')
      if (details && details.length > 0) {
          details.forEach(detail => {
              closeDetails(detail)
          })
      }
  })

  closeDetailsButtons.forEach(button => {
      button.addEventListener('click', () => {
          const details = button.closest('.details')
          closeDetails(details)
      })
  })

  function openDetails(details) {
      if (details == null) return
      details.classList.add('active')
      overlay.classList.add('active')
  }

  function closeDetails(details) {
      if (details == null) return
      details.classList.remove('active')
      overlay.classList.remove('active')
  }
})
