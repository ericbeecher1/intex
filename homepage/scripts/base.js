/* //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
/* //// Nine.js v2.0 ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
/* //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */


/* //// (1) PLUGINS /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */


    /*!
    * hoverIntent v1.8.1 // 2014.08.11 // jQuery v1.9.1+
    * http://briancherne.github.io/jquery-hoverIntent/
    */
    !function(e){"use strict";"function"==typeof define&&define.amd?define(["jquery"],e):jQuery&&!jQuery.fn.hoverIntent&&e(jQuery)}(function(e){"use strict";var t,n,o={interval:100,sensitivity:6,timeout:0},i=0,u=function(e){t=e.pageX,n=e.pageY},r=function(e,o,i,v){return Math.sqrt((i.pX-t)*(i.pX-t)+(i.pY-n)*(i.pY-n))<v.sensitivity?(o.off(i.event,u),delete i.timeoutId,i.isActive=!0,e.pageX=t,e.pageY=n,delete i.pX,delete i.pY,v.over.apply(o[0],[e])):(i.pX=t,i.pY=n,i.timeoutId=setTimeout(function(){r(e,o,i,v)},v.interval),void 0)},v=function(e,t,n,o){return delete t.data("hoverIntent")[n.id],o.apply(t[0],[e])};e.fn.hoverIntent=function(t,n,a){var s=i++,d=e.extend({},o);e.isPlainObject(t)?(d=e.extend(d,t),e.isFunction(d.out)||(d.out=d.over)):d=e.isFunction(n)?e.extend(d,{over:t,out:n,selector:a}):e.extend(d,{over:t,out:t,selector:n});var f=function(t){var n=e.extend({},t),o=e(this),i=o.data("hoverIntent");i||o.data("hoverIntent",i={});var a=i[s];a||(i[s]=a={id:s}),a.timeoutId&&(a.timeoutId=clearTimeout(a.timeoutId));var f=a.event="mousemove.hoverIntent.hoverIntent"+s;if("mouseenter"===t.type){if(a.isActive)return;a.pX=n.pageX,a.pY=n.pageY,o.off(f,u).on(f,u),a.timeoutId=setTimeout(function(){r(n,o,a,d)},d.interval)}else{if(!a.isActive)return;o.off(f,u),a.timeoutId=setTimeout(function(){v(n,o,a,d.out)},d.timeout)}};return this.on({"mouseenter.hoverIntent":f,"mouseleave.hoverIntent":f},d.selector)}});




    /*!
     * parallax.js v1.5.0 (http://pixelcog.github.io/parallax.js/)
     * @copyright 2016 PixelCog, Inc.
     * @license MIT (https://github.com/pixelcog/parallax.js/blob/master/LICENSE)
     */
    !function(t,i,e,s){function o(i,e){var h=this;"object"==typeof e&&(delete e.refresh,delete e.render,t.extend(this,e)),this.$element=t(i),!this.imageSrc&&this.$element.is("img")&&(this.imageSrc=this.$element.attr("src"));var r=(this.position+"").toLowerCase().match(/\S+/g)||[];if(r.length<1&&r.push("center"),1==r.length&&r.push(r[0]),"top"!=r[0]&&"bottom"!=r[0]&&"left"!=r[1]&&"right"!=r[1]||(r=[r[1],r[0]]),this.positionX!==s&&(r[0]=this.positionX.toLowerCase()),this.positionY!==s&&(r[1]=this.positionY.toLowerCase()),h.positionX=r[0],h.positionY=r[1],"left"!=this.positionX&&"right"!=this.positionX&&(isNaN(parseInt(this.positionX))?this.positionX="center":this.positionX=parseInt(this.positionX)),"top"!=this.positionY&&"bottom"!=this.positionY&&(isNaN(parseInt(this.positionY))?this.positionY="center":this.positionY=parseInt(this.positionY)),this.position=this.positionX+(isNaN(this.positionX)?"":"px")+" "+this.positionY+(isNaN(this.positionY)?"":"px"),navigator.userAgent.match(/(iPod|iPhone|iPad)/))return this.imageSrc&&this.iosFix&&!this.$element.is("img")&&this.$element.css({backgroundImage:"url("+this.imageSrc+")",backgroundSize:"cover",backgroundPosition:this.position}),this;if(navigator.userAgent.match(/(Android)/))return this.imageSrc&&this.androidFix&&!this.$element.is("img")&&this.$element.css({backgroundImage:"url("+this.imageSrc+")",backgroundSize:"cover",backgroundPosition:this.position}),this;this.$mirror=t("<div />").prependTo(this.mirrorContainer);var a=this.$element.find(">.parallax-slider"),n=!1;0==a.length?this.$slider=t("<img />").prependTo(this.$mirror):(this.$slider=a.prependTo(this.$mirror),n=!0),this.$mirror.addClass("parallax-mirror").css({visibility:"hidden",zIndex:this.zIndex,position:"fixed",top:0,left:0,overflow:"hidden"}),this.$slider.addClass("parallax-slider").one("load",function(){h.naturalHeight&&h.naturalWidth||(h.naturalHeight=this.naturalHeight||this.height||1,h.naturalWidth=this.naturalWidth||this.width||1),h.aspectRatio=h.naturalWidth/h.naturalHeight,o.isSetup||o.setup(),o.sliders.push(h),o.isFresh=!1,o.requestRender()}),n||(this.$slider[0].src=this.imageSrc),(this.naturalHeight&&this.naturalWidth||this.$slider[0].complete||a.length>0)&&this.$slider.trigger("load")}!function(){for(var t=0,e=["ms","moz","webkit","o"],s=0;s<e.length&&!i.requestAnimationFrame;++s)i.requestAnimationFrame=i[e[s]+"RequestAnimationFrame"],i.cancelAnimationFrame=i[e[s]+"CancelAnimationFrame"]||i[e[s]+"CancelRequestAnimationFrame"];i.requestAnimationFrame||(i.requestAnimationFrame=function(e){var s=(new Date).getTime(),o=Math.max(0,16-(s-t)),h=i.setTimeout(function(){e(s+o)},o);return t=s+o,h}),i.cancelAnimationFrame||(i.cancelAnimationFrame=function(t){clearTimeout(t)})}(),t.extend(o.prototype,{speed:.2,bleed:0,zIndex:-100,iosFix:!0,androidFix:!0,position:"center",overScrollFix:!1,mirrorContainer:"body",refresh:function(){this.boxWidth=this.$element.outerWidth(),this.boxHeight=this.$element.outerHeight()+2*this.bleed,this.boxOffsetTop=this.$element.offset().top-this.bleed,this.boxOffsetLeft=this.$element.offset().left,this.boxOffsetBottom=this.boxOffsetTop+this.boxHeight;var t,i=o.winHeight,e=o.docHeight,s=Math.min(this.boxOffsetTop,e-i),h=Math.max(this.boxOffsetTop+this.boxHeight-i,0),r=this.boxHeight+(s-h)*(1-this.speed)|0,a=(this.boxOffsetTop-s)*(1-this.speed)|0;r*this.aspectRatio>=this.boxWidth?(this.imageWidth=r*this.aspectRatio|0,this.imageHeight=r,this.offsetBaseTop=a,t=this.imageWidth-this.boxWidth,"left"==this.positionX?this.offsetLeft=0:"right"==this.positionX?this.offsetLeft=-t:isNaN(this.positionX)?this.offsetLeft=-t/2|0:this.offsetLeft=Math.max(this.positionX,-t)):(this.imageWidth=this.boxWidth,this.imageHeight=this.boxWidth/this.aspectRatio|0,this.offsetLeft=0,t=this.imageHeight-r,"top"==this.positionY?this.offsetBaseTop=a:"bottom"==this.positionY?this.offsetBaseTop=a-t:isNaN(this.positionY)?this.offsetBaseTop=a-t/2|0:this.offsetBaseTop=a+Math.max(this.positionY,-t))},render:function(){var t=o.scrollTop,i=o.scrollLeft,e=this.overScrollFix?o.overScroll:0,s=t+o.winHeight;this.boxOffsetBottom>t&&this.boxOffsetTop<=s?(this.visibility="visible",this.mirrorTop=this.boxOffsetTop-t,this.mirrorLeft=this.boxOffsetLeft-i,this.offsetTop=this.offsetBaseTop-this.mirrorTop*(1-this.speed)):this.visibility="hidden",this.$mirror.css({transform:"translate3d("+this.mirrorLeft+"px, "+(this.mirrorTop-e)+"px, 0px)",visibility:this.visibility,height:this.boxHeight,width:this.boxWidth}),this.$slider.css({transform:"translate3d("+this.offsetLeft+"px, "+this.offsetTop+"px, 0px)",position:"absolute",height:this.imageHeight,width:this.imageWidth,maxWidth:"none"})}}),t.extend(o,{scrollTop:0,scrollLeft:0,winHeight:0,winWidth:0,docHeight:1<<30,docWidth:1<<30,sliders:[],isReady:!1,isFresh:!1,isBusy:!1,setup:function(){function s(){if(p==i.pageYOffset)return i.requestAnimationFrame(s),!1;p=i.pageYOffset,h.render(),i.requestAnimationFrame(s)}if(!this.isReady){var h=this,r=t(e),a=t(i),n=function(){o.winHeight=a.height(),o.winWidth=a.width(),o.docHeight=r.height(),o.docWidth=r.width()},l=function(){var t=a.scrollTop(),i=o.docHeight-o.winHeight,e=o.docWidth-o.winWidth;o.scrollTop=Math.max(0,Math.min(i,t)),o.scrollLeft=Math.max(0,Math.min(e,a.scrollLeft())),o.overScroll=Math.max(t-i,Math.min(t,0))};a.on("resize.px.parallax load.px.parallax",function(){n(),h.refresh(),o.isFresh=!1,o.requestRender()}).on("scroll.px.parallax load.px.parallax",function(){l(),o.requestRender()}),n(),l(),this.isReady=!0;var p=-1;s()}},configure:function(i){"object"==typeof i&&(delete i.refresh,delete i.render,t.extend(this.prototype,i))},refresh:function(){t.each(this.sliders,function(){this.refresh()}),this.isFresh=!0},render:function(){this.isFresh||this.refresh(),t.each(this.sliders,function(){this.render()})},requestRender:function(){var t=this;t.render(),t.isBusy=!1},destroy:function(e){var s,h=t(e).data("px.parallax");for(h.$mirror.remove(),s=0;s<this.sliders.length;s+=1)this.sliders[s]==h&&this.sliders.splice(s,1);t(e).data("px.parallax",!1),0===this.sliders.length&&(t(i).off("scroll.px.parallax resize.px.parallax load.px.parallax"),this.isReady=!1,o.isSetup=!1)}});var h=t.fn.parallax;t.fn.parallax=function(s){return this.each(function(){var h=t(this),r="object"==typeof s&&s;this==i||this==e||h.is("body")?o.configure(r):h.data("px.parallax")?"object"==typeof s&&t.extend(h.data("px.parallax"),r):(r=t.extend({},h.data(),r),h.data("px.parallax",new o(this,r))),"string"==typeof s&&("destroy"==s?o.destroy(this):o[s]())})},t.fn.parallax.Constructor=o,t.fn.parallax.noConflict=function(){return t.fn.parallax=h,this},t(function(){t('[data-parallax="scroll"]').parallax()})}(jQuery,window,document);



/* //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
/* //// (2) HELPERS /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
/* //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */


    // Logo swap
    // assumes transparent is 'on dark'
    // --------------------------------
    function logo_swap()
    {
        // If desktop
        if($(window).width() > 992)
    	{
            var logo = $('header .logo img');

            // IF header is dark
            if(
                logo.attr('data-on-dark')
                 && ((!$('body header').hasClass('scrolled') && $('body').hasClass('h-transparent')) || $('body').hasClass('h-dark'))
            )
                logo.attr('src', logo.data('on-dark'));

            // ELSE IF header is light
            else if(
                logo.attr('data-on-light')
            )
                logo.attr('src', logo.data('on-light'));
        }

        else
        {
            var logo = $('header .mobile-logo img');

            // IF header is dark
            if(logo.attr('data-on-dark') && $('body').hasClass('h-dark'))
                logo.attr('src', logo.data('on-dark'));

            // ELSE IF header is light
            else if(logo.attr('data-on-light'))
                logo.attr('src', logo.data('on-light'));
        }

    }


    // Show more Box
    // -------------
    function show_more_box()
    {
        $('div.show-more').each(function()
        {
            var box = $(this);
            var box_height = box.attr('data-show-more-height') ? $(this).data('show-more-height') : 300;
            var min_width = box.attr('data-show-more-min-width') ? $(this).data('show-more-min-width') : 'all';
            var max_width = box.attr('data-show-more-max-width') ? $(this).data('show-more-max-width') : 'all';
            var show_more_text = box.attr('data-show-more-open-text') ? $(this).data('show-more-open-text') : 'See More';
            var show_less_text = box.attr('data-show-more-close-text') ? $(this).data('show-more-close-text') : 'See Less';

            if((min_width == 'all' || $(window).width() >= min_width) && (max_width == 'all' || $(window).width() <= max_width))
            {
                // (1) add show-more/less text
                if(box.find('div.show-more-button').length == 0)
                    box.append('<div class="show-more-button"><span class="text">' + show_more_text + '</span></div>');

                box.animate({ height: box_height + 'px' });
                box.children('div.show-more-button').click(function()
                {
                    var cur_text = $(this).children('span.text');
                    if(box.hasClass('open'))
                    {
                        box.removeClass('open');
                        box.stop(true, true).animate({ height: box_height + 'px' });
                        cur_text.html(show_more_text);
                    }
                    else
                    {
                        box.stop(true, true).animate({ height: box.get(0).scrollHeight }, 800,
                        function()
                        {
                            box.addClass('open');
                            box.height('auto');
                            cur_text.html(show_less_text);
                        });

                    }
                });
            }
        });
    }




/* //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
/* //// (3) GO NINE GO ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
/* //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */

/* on resize */
$(window).resize(function()
{
    logo_swap();
});

/* on doc ready */
$(document).ready(function()
{

    // NINE: on ready
    // --------------
    show_more_box();

        // DEMO: header class changer

            logo_swap();

            // setup
            var hcs = $('body').attr('class');
            var header_classes = hcs.split(' ');
            var header_classes_length = header_classes.length;
            for (var i = 0; i < header_classes_length; i++)
            {
                $('.flyout-sticky input[value="' + header_classes[i] + '"]').prop('checked', true);
            }

            // change
            $('.flyout-sticky input').change(function()
            {
                $('body').removeClass();
                $('.flyout-sticky input:checked').each(function(){ $('body').addClass( $(this).val()); });

                logo_swap();
                $(window).trigger('resize');
            });

        // :END DEMO


        // Rotate / Polaroid
        // -----------------

            $("img.img-polaroid, .rotate").each(function()
    		{
    			var rNum = (Math.random() * 4) * (Math.round(Math.random()) * 2 - 1);
    			$(this).css({ '-webkit-transform': 'rotate(' + rNum + '2deg)', '-moz-transform': 'rotate(' + rNum + '2deg)' });
    		});


        // Overlays
        // --------

            $('section.bg-overlay').each(function()
            {
                if($(this).find('div.overlay').length == 0)
                    $(this).wrapInner('<div class="overlay"></div>');
            });

            $('div.abstract-overlay').each(function()
            {
                if($(this).find('div.img-overlay').length == 0)
                    $(this).wrapInner('<div class="img-overlay"></div>');
            });


        // Tab Sections
        // ------------

            $('section.has-tabs').each(function()
            {
                var next_section = $(this).next('section');

                /* bg-gray */
                if(next_section.hasClass('bg-gray'))
                    $(this).addClass('tabs-active-gray');

                /* bg-dark */
                else if(next_section.hasClass('bg-dark'))
                    $(this).addClass('tabs-active-dark');

                /* bg-image */
                else if(next_section.hasClass('bg-image'))
                    $(this).addClass('tabs-active-image');
            });



        // Section Images
        // --------------
        $('img.section-image').closest('section').css('overflow', 'hidden');


        // Tooltips
        // --------
        $('[data-toggle="tooltip"]').tooltip();


        // Flyout sticky
        // -------------
        $('div.flyout-sticky').hover(function()
        {
            $(this).stop(true, true).toggleClass('over');
        });



        // Events
        // ------
        $('[data-fire-event-click]').click(function()
        {
            if(typeof ga == 'function')
            {
                var parts = $(this).data('fire-event-click').split(',');

                // IF element has it's own analytics info
                if($(this).attr('data-analytics-info'))
                {
                    var parts2 = $(this).data('analytics-info').split(',');
                    ga('create', parts2[0], 'auto', parts2[1]);
                    ga(parts2[1] + '.send', 'event', parts[0], parts[1], parts[2]);
                }

                // ELSE default
                else
                    ga('send', 'event', parts[0], parts[1], parts[2]);

            }

        });

            $('[data-fire-event-load]').each(function()
            {
                if(typeof ga == 'function')
                {
                    var parts = $(this).data('fire-event-load').split(',');

                    // IF element has it's own analytics info
                    if($(this).attr('data-analytics-info'))
                    {
                        var parts2 = $(this).data('analytics-info').split(',');
                        ga('create', parts2[0], 'auto', parts2[1]);
                        ga(parts2[1] + '.send', 'event', parts[0], parts[1], parts[2]);
                    }

                    // ELSE default
                    else
                        ga('send', 'event', parts[0], parts[1], parts[2]);
                }

            });



        // Forms
        // -----
        $('form[data-ajax-action]').submit(function(event)
        {
            event.preventDefault();

            tf = $(this);
            tfd = tf.serialize();
            tf.animate({opacity: .5});

            // IF reCAPTCHA
            if(typeof grecaptcha == 'object' && tf.attr('data-recaptcha'))
            {
                var action_name = 'From';
                if(tf.attr('data-form-info'))
                    action_name = tf.data('form-info');

                try
                {
                    grecaptcha.execute(tf.data('recaptcha'), {action: action_name}).then(function(token)
                    {
                        tfd += '&recaptcha_token=' + token;
                        submit_form(tf, tfd);
                    });
                }
                catch(err)
                {
                    alert('Sorry, there was an error. Please call us directly.');
                    console.log('Error with reCAPTCHA: ' + err);
                }
            }

            // ELSE submit now
            else
                submit_form(tf, tfd);

        });

            function submit_form(the_form, the_form_data)
            {
                var form_wrapper = the_form.parent('div.oak_contact_form_wrapper');
                var above_form = form_wrapper.children('div.oak_contact_above_form');
                var below_form = form_wrapper.children('div.oak_contact_below_form');

                // Notify user of submission
                above_form.stop(true, true).slideUp();
                above_form.html('<div role="alert" class="alert alert-info" style="margin-bottom: 4px;"><strong>Sending...</strong> please wait.</div>');
                above_form.stop(true, true).slideDown();

                // Ajax
                $.ajax(
                {
                    type: 'POST',
                    url: the_form.data('ajax-action'),
                    data: the_form_data,
                    success: function(return_data)
                    {
                        rdo = $.parseJSON(return_data);

                        switch(rdo.result.type)
                        {
                            case 'success':

                                // If redirect
                                if(rdo.result.redirect_to != '')
                                    window.location = rdo.result.redirect_to;

                                else
                                {
                                    // If google event
                                    if(rdo.result.fire_google_event != null && rdo.result.fire_google_event != '' && typeof ga == 'function')
                                    {
                                        console.log('fired google event: ' + rdo.result.fire_google_event);

                                        // IF form has it's own analytics info
                                        if(rdo.result.analytics_info != '')
                                        {
                                            var parts2 = rdo.result.analytics_info.split(',');
                                            ga('create', parts2[0], 'auto', parts2[1]);
                                            ga(parts2[1] + '.send', 'event', rdo.result.fire_google_event, 'submit', 'success');
                                        }

                                        // ELSE default
                                        else
                                            ga('send', 'event', rdo.result.fire_google_event, 'submit', 'success');
                                    }

                                    above_form.stop(true, true).slideUp();
                                    above_form.html('<div role="alert" class="alert alert-success" style="margin-bottom: 4px;">' + rdo.result.message + '</div>')
                                    above_form.stop(true, true).slideDown();

                                    //the_form.stop(true, true).animate({opacity: 1}); // Show form after success
                                    the_form.stop(true, true).slideUp(); // Hide form after success
                                }
                                break;

                            default:
                                above_form.stop(true, true).slideUp();
                                above_form.html('<div role="alert" class="alert alert-' + rdo.result.type + '" style="margin-bottom: 4px;">' + rdo.result.message + '</div>')
                                above_form.stop(true, true).slideDown();

                                the_form.stop(true, true).animate({opacity: 1});
                                break;
                        }
                    },

                    error: function()
                    {
                        above_form.stop(true, true).slideUp();
                        above_form.html('<div role="alert" class="alert alert-error" style="margin-bottom: 4px;"><strong>Ops!</strong> Something went wrong. Please call us if this message persists.</div>')
                        above_form.stop(true, true).slideDown();

                        //the_form.find('input, select, textarea').prop('disabled', false);
                        the_form.stop(true, true).animate({opacity: 1});
                    }

                });
            }


    // Bootstrap Carousels
    // -------------------
    $('.carousel').each(function()
    {
        // Vars
        var id = $(this).attr('id');
        var items = $(this).find('.carousel-item');
        var indicators = $(this).find('ol.carousel-indicators');

        // Set active
        items.first().addClass('active');

        // Set indicators
        for(i = 0; i < items.length; i++)
        {
            var active = (i == 0) ? ' class="active"' : '';
            indicators.append('<li data-target="#' + id + '" data-slide-to="' + i + '"' + active + '></li>');
        }

    });


    // Header Search
    // -------------
    $('.toggle-header-search').click(function(e)
    {
        e.preventDefault();
        $('header .logo, header nav, body.h-show-icon-group header .icon-group, header .header-search').toggle();
        $('header .header-search input[name=q]').focus();
    });

        $('a.submit-header-search').click(function(e)
        {
            e.preventDefault();
            $('header .header-search form').submit();
        });


    if($(window).width() > 992)
	{
        // NINE: Sticky Header
        // -------------------
        if($(this).scrollTop() > 45)
        {
            $('body, header').addClass('scrolled');
            logo_swap();
        }

        $(document).scroll(function()
        {
            if($(this).scrollTop() > 45)
            {
                // Close sticky mega on scroll
                $('body.h-sticky header nav > ul > li.mega > ul').fadeOut('fast');
                $('body, header').addClass('scrolled');
                logo_swap();
            }
            else
            {
                $('body, header').removeClass('scrolled');
                logo_swap();
            }

        });

        // NINE: Menu
        // -----------

        // Hover intent
		var config = {
						sensitivity: 2, 	// number = sensitivity threshold (must be 1 or higher)
						interval: 100, 		// number = milliseconds for onMouseOver polling interval
						over: mega_over,	// function = onMouseOver callback (REQUIRED)
						timeout: 400,		// number = milliseconds delay before onMouseOut
						out: mega_out		// function = onMouseOut callback (REQUIRED)
					};

        // Mega
        // ----
		var mega = $('nav > ul > li.mega');
        mega.hoverIntent(config);
		mega.hover(function()
		{
            // Re-adjust the top position based off the current bottom position of level_1
            $('li.mega ul.level-2').css('top', $(this).position().top + $(this).outerHeight(true));

            // Update z-indexing to show on top
			$('ul.level-2').css('z-index', 99);
			$(this).find('ul.level-2').css('z-index', 100);
			$(this).children('a').addClass('over');
		},
		function()
		{
			$(this).children('a').removeClass('over');
		});


        // Hover intent
		var config2 = {
						sensitivity: 2, 	// number = sensitivity threshold (must be 1 or higher)
						interval: 100, 		// number = milliseconds for onMouseOver polling interval
						over: flyout_over,	// function = onMouseOver callback (REQUIRED)
						timeout: 400,		// number = milliseconds delay before onMouseOut
						out: flyout_out		// function = onMouseOut callback (REQUIRED)
					};

        // Flyout
        // ------
        $('nav > ul > li.flyout').hoverIntent(config2);
        $('nav ul li.flyout li').hoverIntent(config2);
		$('nav ul li.flyout li, nav > ul > li.flyout').hover(function()
		{
            // Update z-indexing to show on top
			$('ul.level-2').css('z-index', 99);
			$(this).find('ul.level-2').css('z-index', 100);
			$(this).children('a').addClass('over');
		},
		function()
		{
			$(this).children('a').removeClass('over');
		});

	}
    else
    {
        // NINE: Mobile sub
    	// ----------------
    	$('nav ul.level-1 li a.parent').click(function(e)
    	{
    		e.preventDefault();
            var a1 = $(this);
    		var ul2 = $(this).next('ul.level-2');

    		ul2.stop(true, true).slideToggle('fast', function()
    		{
    			if($(this).is(':visible'))
    				a1.addClass('open');

    			else
    				a1.removeClass('open');

    		});
    	});
    }

        function mega_over() { $(this).children('ul').fadeIn('fast').css('display', 'flex'); }
    	function mega_out() { $(this).children('ul').fadeOut('fast'); }

        function flyout_over() { $(this).children('ul').fadeIn('fast'); }
    	function flyout_out() { $(this).children('ul').fadeOut('fast'); }


    // NINE: Mobile menu
	// -----------------
	$('header div.mobile-nav-trigger').click(function()
	{
		$('header div.mobile-nav-trigger, header div.mobile-icon-group, nav').toggleClass('open');
	});


    // Parallax
    //  do last for proper window size
    // -------------------------------
    $('[data-parallax-image]').each(function()
    {
        var path = $(this).data('parallax-image');
        if(path != '')
            $(this).parallax({ imageSrc: path });
    });

});
