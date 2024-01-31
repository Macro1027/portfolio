
import streamlit as st
import streamlit.components.v1 as components

# -----------------  tableau  -----------------  #
with st.container():
    st.markdown("""""")
    st.subheader("📊 Tableau")
    col1,col2 = st.columns([0.95, 0.05])
    with col1:
        with st.expander('See the work'):
            components.html(
                """
                <!DOCTYPE html>
                <html>  
                    <title>Basic HTML</title>  
                    <body style="width:130%">  
                        <div class='tableauPlaceholder' id='viz1684205791200' style='position: static'><noscript><a href='#'><img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Su&#47;SunnybrookTeam&#47;Overview&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='SunnybrookTeam&#47;Overview' /><param name='tabs' value='yes' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Su&#47;SunnybrookTeam&#47;Overview&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1684205791200');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.minWidth='1350px';vizElement.style.maxWidth='100%';vizElement.style.minHeight='1550px';vizElement.style.maxHeight=(divElement.offsetWidth*0.75)+'px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.minWidth='1350px';vizElement.style.maxWidth='100%';vizElement.style.minHeight='1550px';vizElement.style.maxHeight=(divElement.offsetWidth*0.75)+'px';} else { vizElement.style.width='100%';vizElement.style.minHeight='5750px';vizElement.style.maxHeight=(divElement.offsetWidth*1.77)+'px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>
                    </body>  
                </HTML>
                """
            , height=400, scrolling=True
            )
    st.markdown(""" <a href={}> <em>🔗 access to the link </a>""".format(info['Tableau']), unsafe_allow_html=True)
    
# ----------------- medium ----------------- #
with st.container():
    st.markdown("""""")
    st.subheader('✍️ Medium')
    col1,col2 = st.columns([0.95, 0.05])
    with col1:
        with st.expander('Display my latest posts'):
            components.html(embed_rss['rss'],height=400)
            
        st.markdown(""" <a href={}> <em>🔗 access to the link </a>""".format(info['Medium']), unsafe_allow_html=True)

# -----------------  endorsement  ----------------- #
with st.container():
    # Divide the container into three columns
    col1,col2,col3 = st.columns([0.475, 0.475, 0.05])
    # In the first column (col1)        
    with col1:
        # Add a subheader to introduce the coworker endorsement slideshow
        st.subheader("👄 Coworker Endorsements")
        # Embed an HTML component to display the slideshow
        components.html(
        f"""
        <!DOCTYPE html>
        <html>
        <head>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <!-- Styles for the slideshow -->
        <style>
            * {{box-sizing: border-box;}}
            .mySlides {{display: none;}}
            img {{vertical-align: middle;}}

            /* Slideshow container */
            .slideshow-container {{
            position: relative;
            margin: auto;
            width: 100%;
            }}

            /* The dots/bullets/indicators */
            .dot {{
            height: 15px;
            width: 15px;
            margin: 0 2px;
            background-color: #eaeaea;
            border-radius: 50%;
            display: inline-block;
            transition: background-color 0.6s ease;
            }}

            .active {{
            background-color: #6F6F6F;
            }}

            /* Fading animation */
            .fade {{
            animation-name: fade;
            animation-duration: 1s;
            }}

            @keyframes fade {{
            from {{opacity: .4}} 
            to {{opacity: 1}}
            }}

            /* On smaller screens, decrease text size */
            @media only screen and (max-width: 300px) {{
            .text {{font-size: 11px}}
            }}
            </style>
        </head>
        <body>
            <!-- Slideshow container -->
            <div class="slideshow-container">
                <div class="mySlides fade">
                <img src={endorsements["img1"]} style="width:100%">
                </div>

                <div class="mySlides fade">
                <img src={endorsements["img2"]} style="width:100%">
                </div>

                <div class="mySlides fade">
                <img src={endorsements["img3"]} style="width:100%">
                </div>

            </div>
            <br>
            <!-- Navigation dots -->
            <div style="text-align:center">
                <span class="dot"></span> 
                <span class="dot"></span> 
                <span class="dot"></span> 
            </div>

            <script>
            let slideIndex = 0;
            showSlides();

            function showSlides() {{
            let i;
            let slides = document.getElementsByClassName("mySlides");
            let dots = document.getElementsByClassName("dot");
            for (i = 0; i < slides.length; i++) {{
                slides[i].style.display = "none";  
            }}
            slideIndex++;
            if (slideIndex > slides.length) {{slideIndex = 1}}    
            for (i = 0; i < dots.length; i++) {{
                dots[i].className = dots[i].className.replace("active", "");
            }}
            slides[slideIndex-1].style.display = "block";  
            dots[slideIndex-1].className += " active";
            }}

            var interval = setInterval(showSlides, 2500); // Change image every 2.5 seconds

            function pauseSlides(event)
            {{
                clearInterval(interval); // Clear the interval we set earlier
            }}
            function resumeSlides(event)
            {{
                interval = setInterval(showSlides, 2500);
            }}
            // Set up event listeners for the mySlides
            var mySlides = document.getElementsByClassName("mySlides");
            for (i = 0; i < mySlides.length; i++) {{
            mySlides[i].onmouseover = pauseSlides;
            mySlides[i].onmouseout = resumeSlides;
            }}
            </script>

            </body>
            </html> 

            """,
                height=270,
    )  

# -----------------  contact  ----------------- #
    with col2:
        st.subheader("📨 Contact Me")
        contact_form = f"""
        <form action="https://formsubmit.co/{info["Email"]}" method="POST">
            <input type="hidden" name="_captcha value="false">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Your message here" required></textarea>
            <button type="submit">Send</button>
        </form>
        """
        st.markdown(contact_form, unsafe_allow_html=True)