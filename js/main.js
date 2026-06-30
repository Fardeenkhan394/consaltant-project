(function ($) {
    'use strict';

    /* Page load */
    $('body').addClass('loaded');

    /* Hero slider */
    var $slides = $('#hero .hero-slide');
    if ($slides.length) {
        var $bullets = $('.hero-bullets span');
        var cur = 0;
        var heroTimer;

        function goHero(i) {
            cur = (i + $slides.length) % $slides.length;
            $slides.removeClass('active').eq(cur).addClass('active');
            $bullets.removeClass('selected').eq(cur).addClass('selected');
        }

        function startHero() {
            clearInterval(heroTimer);
            heroTimer = setInterval(function () { goHero(cur + 1); }, 6500);
        }

        $bullets.on('click', function () {
            goHero(parseInt($(this).data('index'), 10));
            startHero();
        });
        startHero();
    }

    /* Mobile menu */
    $('.menu-toggle').on('click', function () {
        $('body').toggleClass('nav-open');
    });
    $(document).on('click', function (e) {
        if ($('body').hasClass('nav-open') && !$(e.target).closest('#header').length) {
            $('body').removeClass('nav-open');
        }
    });

    /* Sticky header */
    var $header = $('#header');

    function setHeaderHeight() {
        var h = $header.outerHeight() || 138;
        var navH = $header.find('.nav-box').outerHeight() || 52;
        document.documentElement.style.setProperty('--header-height', h + 'px');
        document.documentElement.style.setProperty('--nav-height', navH + 'px');
    }

    function onHeaderScroll() {
        var st = $(window).scrollTop();
        if ($('body').hasClass('header_transparent')) {
            $header.toggleClass('scrolled', st > 50);
        } else {
            $header.addClass('scrolled');
        }
        $('#back-top').toggleClass('visible', st > 400);
    }

    $(window).on('scroll', onHeaderScroll);
    $(window).on('load resize', function () {
        setHeaderHeight();
        onHeaderScroll();
    });
    onHeaderScroll();

    /* Smooth scroll */
    $('a[href^="#"]').on('click', function (e) {
        var id = this.getAttribute('href');
        if (id.length > 1) {
            var $t = $(id);
            if ($t.length) {
                e.preventDefault();
                $('html, body').animate({ scrollTop: $t.offset().top - ($header.hasClass('scrolled') ? 56 : 12) }, 600);
                $('body').removeClass('nav-open');
            }
        }
    });

    /* Back to top */
    if (!$('#back-top').length) {
        $('body').append('<button id="back-top" type="button" aria-label="Back to top"><i class="fa fa-chevron-up"></i></button>');
    }
    $('#back-top').on('click', function () {
        $('html, body').animate({ scrollTop: 0 }, 600);
    });

    /* Scroll reveal */
    function revealOnScroll() {
        $('.reveal').each(function () {
            var $el = $(this);
            if ($el.hasClass('revealed')) return;
            var top = $el.offset().top;
            var win = $(window).scrollTop() + $(window).height() * 0.88;
            if (top < win) $el.addClass('revealed');
        });
    }
    $(window).on('scroll load resize', revealOnScroll);
    revealOnScroll();

    /* Services carousel */
    if ($('.services-carousel').length) {
        $('.services-carousel').owlCarousel({
            items: 4,
            loop: true,
            margin: 24,
            nav: true,
            dots: false,
            autoplay: true,
            autoplayTimeout: 5000,
            autoplayHoverPause: true,
            smartSpeed: 600,
            navText: ['<i class="fa fa-angle-left"></i>', '<i class="fa fa-angle-right"></i>'],
            responsive: {
                0: { items: 1 },
                576: { items: 2 },
                992: { items: 3 },
                1200: { items: 4 }
            }
        });
    }

    /* Generic card sliders (sectors, values, PRD difference) */
    if ($('.cards-carousel').length) {
        $('.cards-carousel').each(function () {
            var $c = $(this);
            var big = parseInt($c.attr('data-items'), 10) || 3;
            $c.owlCarousel({
                loop: true,
                margin: 24,
                nav: true,
                dots: true,
                autoplay: true,
                autoplayTimeout: 6000,
                autoplayHoverPause: true,
                smartSpeed: 600,
                navText: ['<i class="fa fa-angle-left"></i>', '<i class="fa fa-angle-right"></i>'],
                responsive: {
                    0: { items: 1 },
                    576: { items: 2 },
                    992: { items: big >= 4 ? 3 : big },
                    1200: { items: big }
                }
            });
        });
    }

    /* Sector filter */
    $('.filter-tabs a').on('click', function (e) {
        e.preventDefault();
        var f = $(this).data('filter');
        $('.filter-tabs a').removeClass('active');
        $(this).addClass('active');
        $('.case-item').each(function () {
            var show = f === 'all' || $(this).data('cat') === f;
            $(this).toggle(show).toggleClass('reveal revealed', show);
        });
    });

    /* Accordion */
    $('.accordion-head').on('click', function () {
        var $p = $(this).closest('.accordion-panel');
        $('.accordion-panel').not($p).removeClass('open');
        $p.toggleClass('open');
    });

    /* Counters */
    var counted = false;
    function animateCounters() {
        if (counted) return;
        $('.counter').each(function () {
            var $el = $(this);
            var target = parseInt($el.data('target'), 10);
            var $suffix = $el.find('span');
            var suffix = $suffix.length ? $suffix.text() : '';
            $({ n: 0 }).animate({ n: target }, {
                duration: 2200,
                easing: 'swing',
                step: function () {
                    $el.html(Math.floor(this.n) + (suffix ? '<span>' + suffix + '</span>' : ''));
                },
                complete: function () {
                    $el.html(target + (suffix ? '<span>' + suffix + '</span>' : ''));
                }
            });
        });
        counted = true;
    }

    $(window).on('scroll load', function () {
        if ($('.counter').length && !counted) {
            var $first = $('.counter').first();
            if ($(window).scrollTop() + $(window).height() > $first.offset().top + 60) {
                animateCounters();
            }
        }
    });

    /* Map location tabs */
    var mapUrls = {
        uk: 'https://www.google.com/maps?q=86+Wind+Road,Ystradgynlais,Swansea,Wales,UK&hl=en&z=14&output=embed',
        isb: 'https://www.google.com/maps?q=25-Huma+Plaza,Fazal-e-Haq+Road,Blue+Area,Islamabad,Pakistan&hl=en&z=15&output=embed',
        hyd: 'https://www.google.com/maps?q=Bakhtawar+Colony,Qasimabad,Hyderabad,Pakistan&hl=en&z=15&output=embed'
    };
    $('.map-tab').on('click', function () {
        var key = $(this).data('map');
        $('.map-tab').removeClass('active');
        $(this).addClass('active');
        if (mapUrls[key]) {
            $('#office-map').attr('src', mapUrls[key]);
        }
    });

    /* Contact form */
    $('#contact-form').on('submit', function (e) {
        e.preventDefault();
        var $btn = $(this).find('button[type="submit"]');
        $btn.prop('disabled', true).text('Sending...');
        setTimeout(function () {
            $btn.prop('disabled', false).text('Send Message');
            alert('Thank you for your message. We will contact you shortly.');
            $('#contact-form')[0].reset();
        }, 800);
    });

    /* Careers application forms */
    var careerMeta = {
        jobs: {
            title: 'Apply for Jobs',
            intro: 'Submit your application for full-time positions at PRD Consultants. Please complete all fields and attach your CV.',
            email: 'info.UK@prdconsultantsltd.com'
        },
        consultancies: {
            title: 'Register for Consultancies',
            intro: 'Join our multidisciplinary network of national and international experts. Share your area of expertise, availability, and relevant development experience.',
            email: 'info.UK@prdconsultantsltd.com'
        },
        internships: {
            title: 'Apply for Internships',
            intro: 'Apply for internship opportunities with PRD Consultants in the United Kingdom or Pakistan.',
            email: 'info.ISB@prdconsultantsltd.com'
        }
    };

    var $careerModal = $('#career-form-modal');
    var $careerBackdrop = $('#career-form-backdrop');
    var $careerForm = $('#career-application-form');

    function setCareerFields(type) {
        $('.career-field').removeClass('is-visible').find('input, select, textarea').prop('required', false);
        $('.career-field-' + type).addClass('is-visible');
        $('.career-field.is-visible').find('input, select, textarea').each(function () {
            var t = $(this).attr('type');
            if (t !== 'file' && t !== 'hidden') $(this).prop('required', true);
        });
        $('#career-cv').prop('required', true);
    }

    function openCareerForm(type) {
        var meta = careerMeta[type];
        if (!meta || !$careerModal.length) return;
        $('#application-type').val(type);
        $('#career-form-title').text(meta.title);
        $('#career-form-intro').text(meta.intro);
        $('.career-card').removeClass('is-active');
        $('.career-card[data-career-type="' + type + '"]').addClass('is-active').attr('aria-expanded', 'true');
        $careerForm[0].reset();
        $('#cv-file-name').text('');
        setCareerFields(type);
        $careerModal.removeAttr('hidden').addClass('is-open');
        $careerBackdrop.removeAttr('hidden').addClass('is-open');
        $('body').addClass('career-modal-open');
        $careerModal.find('input:visible, select:visible, textarea:visible').first().focus();
    }

    function closeCareerForm() {
        $careerModal.removeClass('is-open').attr('hidden', true);
        $careerBackdrop.removeClass('is-open').attr('hidden', true);
        $('body').removeClass('career-modal-open');
        $('.career-card').removeClass('is-active').attr('aria-expanded', 'false');
    }

    $('.career-card[data-career-type]').on('click', function () {
        openCareerForm($(this).data('career-type'));
    });
    $('.career-form-close, #career-form-backdrop').on('click', closeCareerForm);
    $(document).on('keydown', function (e) {
        if (e.key === 'Escape' && $careerModal.hasClass('is-open')) closeCareerForm();
    });

    $('#career-cv').on('change', function () {
        var file = this.files && this.files[0];
        if (!file) { $('#cv-file-name').text(''); return; }
        if (file.size > 5 * 1024 * 1024) {
            alert('File size must be under 5MB.');
            this.value = '';
            $('#cv-file-name').text('');
            return;
        }
        $('#cv-file-name').text('Selected: ' + file.name);
    });

    $careerForm.on('submit', function (e) {
        e.preventDefault();
        var type = $('#application-type').val();
        var meta = careerMeta[type];
        var lines = ['Application Type: ' + type.toUpperCase(), ''];
        $(this).find('input, select, textarea').not('[type="file"]').not('[type="hidden"]').each(function () {
            var $f = $(this);
            var $group = $f.closest('.career-field');
            if ($group.length && !$group.hasClass('is-visible')) return;
            var name = $f.attr('name');
            if (!name || $f.attr('type') === 'file') return;
            var label = $f.attr('placeholder') || name;
            lines.push(label.replace(' *', '') + ': ' + ($f.val() || ''));
        });
        var cvName = $('#career-cv')[0].files[0] ? $('#career-cv')[0].files[0].name : '(not attached)';
        lines.push('', 'CV File: ' + cvName);
        var subject = 'PRD Careers Application – ' + meta.title;
        var body = lines.join('\n');
        window.location.href = 'mailto:' + meta.email +
            '?subject=' + encodeURIComponent(subject) +
            '&body=' + encodeURIComponent(body);
        setTimeout(function () {
            alert('Your email application will open. Please attach your CV file before sending.\n\nAlternatively email your CV to ' + meta.email);
            closeCareerForm();
        }, 300);
    });

    var hash = window.location.hash.replace('#', '');
    if (careerMeta[hash]) openCareerForm(hash);
})(jQuery);
