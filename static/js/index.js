$(document).ready( function () {
    $('#search-btn').on('click', function (e) {
        e.preventDefault();
        const searchText = $('#search-box').val();
        $.ajax({
            url: '/menu?search_filter=' + searchText,
            type: 'GET',
            success: function (resp) {
                const newHtml = resp.data.map(d => {
                    return `<div class="pizza-item">
                            <img src="${d.image}" style="display:inline-block" alt="">
                                <div class="pizza-text-box">
                                    <h4>${d.name}</h4>
                                    <p>${d.price} kr</p>
                                    <a href="/menu/${d.id}">
                                        <button>View details</button>
                                    </a>
                                </div>
                            </div>`
                });
                $('.pizza').html(newHtml.join(''));
                $('#search-box').val('');
            },
            errors: function (xhr, status, error) {
                console.log(error)
            }
        })
    })
});


$(document).ready( function () {
    $('.add-button-pizza').on('click', function (e) {
        e.preventDefault();
        const pizza_id = $(this).parent().attr('id');
        let elem = $(this).siblings('.amount');
        let minus_btn = $(this).siblings('.minus-button-pizza');
        let checkout_btn = $('.checkout');
        $.ajax({
            url: '/cart?add-pizza=' + pizza_id,
            type: 'GET',
            success: function (resp) {
                const [new_amount, new_price] = resp.data;
                if (new_amount > 0) {
                     minus_btn.prop('disabled',false)
                }
                if (new_price > 0) {
                     checkout_btn.prop('disabled',false)
                }
                $('.price').text(`Price: ${new_price} kr`);
                elem.text(new_amount);

            },
            errors: function (xhr, status, error) {
                console.log(error)
            }
        })
    })
});


$(document).ready( function () {
    $('.minus-button-pizza').on('click', function (e) {
        e.preventDefault();
        const pizza_id = $(this).parent().attr('id');
        let elem = $(this).siblings('.amount');
        let btn = $(this);
        let checkout_btn = $('.checkout');
        $.ajax({
            url: '/cart?minus-pizza=' + pizza_id,
            type: 'GET',
            success: function (resp) {
                const [new_amount, new_price] = resp.data;
                if (new_amount < 1) {
                     btn.prop('disabled',true)
                }
                if (new_price < 1) {
                     checkout_btn.prop('disabled', true)
                }
                $('.price').text(`Price: ${new_price} kr`);
                elem.text(new_amount);
            },
            errors: function (xhr, status, error) {
                console.log(error)
            }
        })
    })
});


$(document).ready( function () {
    $('.add-button-offer').on('click', function (e) {
        e.preventDefault();
        const pizza_id = $(this).parent().attr('id');
        let elem = $(this).siblings('.amount');
        let minus_btn = $(this).siblings('.minus-button-offer');
        let checkout_btn = $('.checkout');
        $.ajax({
            url: '/cart?add-offer=' + pizza_id,
            type: 'GET',
            success: function (resp) {
                const [new_amount, new_price] = resp.data;
                if (new_amount > 0) {
                     minus_btn.prop('disabled',false)
                }
                if (new_price > 0) {
                     checkout_btn.prop('disabled', false)
                }
                $('.price').text(`Price: ${new_price} kr`);
                elem.text(new_amount);
            },
            errors: function (xhr, status, error) {
                console.log(error)
            }
        })
    })
});


$(document).ready( function () {
    $('.minus-button-offer').on('click', function (e) {
        e.preventDefault();
        const pizza_id = $(this).parent().attr('id');
        let elem = $(this).siblings('.amount');
        let btn = $(this);
        let checkout_btn = $('.checkout');
        $.ajax({
            url: '/cart?minus-offer=' + pizza_id,
            type: 'GET',
            success: function (resp) {
                const [new_amount, new_price] = resp.data;
                if (new_amount < 1) {
                     btn.prop('disabled',true)
                }
                if (new_price < 1) {
                     checkout_btn.prop('disabled', true)
                }
                $('.price').text(`Price: ${new_price} kr`);
                elem.text(new_amount);
            },
            errors: function (xhr, status, error) {
                console.log(error)
            }
        })
    })
});

$(document).ready( function () {
    $('.clear-all').on('click', function (e) {
        e.preventDefault();
        $.ajax({
            url: '/cart?clear-all',
            type: 'GET',
            success: function (resp) {
                $('.pizza').empty();
            },
            errors: function (xhr, status, error) {
                console.log(error)
            }
        })
    })
});

$(document).ready( function () {
    $('.remove-button-pizza').on('click', function (e) {
        e.preventDefault();
        const remove_id = $(this).parent().attr('id');
        let elem = $(this).parent();
        let checkout_btn = $('.checkout');
        $.ajax({
            url: '/cart?remove-pizza=' + remove_id,
            type: 'GET',
            success: function (resp) {
                const new_price = resp.data;
                elem.remove();
                if (new_price < 1) {
                     checkout_btn.prop('disabled', true)
                }
                $('.price').text(`Price: ${new_price} kr`);
            },
            errors: function (xhr, status, error) {
                console.log(error)
            }
        })
    })
});


$(document).ready( function () {
    $('.remove-button-offer').on('click', function (e) {
        e.preventDefault();
        const remove_id = $(this).parent().attr('id');
        let elem = $(this).parent();
        let checkout_btn = $('.checkout');
        $.ajax({
            url: '/cart?remove-offer=' + remove_id,
            type: 'GET',
            success: function (resp) {
                const new_price = resp.data;
                elem.remove();
                if (new_price < 1) {
                     checkout_btn.prop('disabled', true)
                }
                $('.price').text(`Price: ${new_price} kr`);
            },
            errors: function (xhr, status, error) {
                console.log(error)
            }
        })
    })
});

$(document).ready( function () {
    $('.sort-by-select').change( function (e) {
        e.preventDefault();
        const elem = $(this).children(":selected").attr('id');
        if (elem === 'name') {
            $.ajax({
                url: '/menu?sort_name',
                type: 'GET',
                success: function (resp) {
                    const newHtml = resp.data.map(d => {
                    return `<div class="pizza-item">
                            <img src="${d.image}" style="display:inline-block" alt="">
                                <div class="pizza-text-box">
                                    <h4>${d.name}</h4>
                                    <p>${d.price} kr</p>
                                    <a href="/menu/${d.id}">
                                        <button>View details</button>
                                    </a>
                                </div>
                            </div>`
                });
                $('.pizza').html(newHtml.join(''));
                },
                errors: function (xhr, status, error) {
                    console.log(error)
                }
            })
        }
        else if (elem === 'price') {
            $.ajax({
                url: '/menu?sort_price',
                type: 'GET',
                success: function (resp) {
                    const newHtml = resp.data.map(d => {
                    return `<div class="pizza-item">
                            <img src="${d.image}" style="display:inline-block" alt="">
                                <div class="pizza-text-box">
                                    <h4>${d.name}</h4>
                                    <p>${d.price} kr</p>
                                    <a href="/menu/${d.id}">
                                        <button>View details</button>
                                    </a>
                                </div>
                            </div>`
                });
                $('.pizza').html(newHtml.join(''));
                },
                errors: function (xhr, status, error) {
                    console.log(error)
                }
            })
        }
    })
});


$(document).ready( function () {
    $('.filter-by-select').change( function (e) {
        e.preventDefault();
        const elem = $(this).children(":selected").attr('id');
        $.ajax({
            url: '/menu?filter=' + elem,
            type: 'GET',
            success: function (resp) {
                const newHtml = resp.data.map(d => {
                return `<div class="pizza-item">
                        <img src="${d.image}" style="display:inline-block" alt="">
                            <div class="pizza-text-box">
                                <h4>${d.name}</h4>
                                <p>${d.price} kr</p>
                                <a href="/menu/${d.id}">
                                    <button>View details</button>
                                </a>
                            </div>
                        </div>`
            });
            $('.pizza').html(newHtml.join(''));
            },
            errors: function (xhr, status, error) {
                console.log(error)
            }
        })
    })
});


/*
$(document).ready( function () {
    $('.add-button').on('click', function (e) {
        e.preventDefault();
        const pizza_id = $(this).parent().attr('id');
        console.log("hey");
        $.ajax({
            url: '/cart?add-pizza=' + pizza_id,
            type: 'GET',
            success: function (resp) {
                const newHtml = resp.data.map(d => {
                    return `<div class="pizza-item" id="${d.id}">
                                <p>${d.name }</p>
                                <p>${d.amount }</p>
                                <button type="button" class="minus-button">-</button>
                                <button type="button" class="add-button">+</button>
                            </div>`
                });
                $('.pizza').html(newHtml.join(''));
            },
            errors: function (xhr, status, error) {
                console.log(error)
            }
        })
    })
});

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


 */
