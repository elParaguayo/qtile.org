var init_demo = function(){
    (function($){
        $(function(){
            var $config = $('section.example .config'),
                config_expander = tmpl('config_expander');

            $config.prepend(config_expander({}));

            $config.find('.btn-toggle')
                .data('expanded', false)
                .attr('title', 'Expand')
                .on('click', function(){
                    var $this = $(this),
                        $icon = $this.find('span.fa'),
                        $pre = $config.find('pre'),
                        scrollHeight = $pre.get(0).scrollHeight,
                        scrollWidth = $pre.get(0).scrollWidth;

                    $this.data('expanded', !$this.data('expanded'));
                    var newHeight = $this.data('expanded') ? scrollHeight : 340;
                    var newWidth = $this.data('expanded') ? scrollWidth : 'auto';

                    $this.attr('title', $this.data('expanded') ? 'Collapse' : 'Expand');
                    $icon.toggleClass('fa-expand').toggleClass('fa-compress');
                    $pre.animate({height: newHeight + 'px', width: newWidth} );
                });

        });
    })(jQuery);
};
