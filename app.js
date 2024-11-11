let viz1, viz2, viz3;

// URLs for the Tableau dashboards
const url1 = "https://public.tableau.com/shared/BS4JR2CW8?:display_count=n&:origin=viz_share_link";
const url2 = "https://public.tableau.com/views/Wolt-Map2/Dashboard2?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link";
const url3 = "https://public.tableau.com/views/Wolt-Citycounter/Citycounterdashboard?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link";


// Options for all dashboards
const options = {
    hideTabs: true,
    height: 800,
    width: 1200,
    onFirstInteraction: function () {
        console.log("Dashboard is interactive");
    }
};

// Functions to initialize each dashboard only when needed
function initViz1() {
    if (!viz1) {
        const vizContainer1 = document.getElementById('vizContainer1');
        viz1 = new tableau.Viz(vizContainer1, url1, options);
    }
}

function initViz2() {
    if (!viz2) {
        const vizContainer2 = document.getElementById('vizContainer2');
        viz2 = new tableau.Viz(vizContainer2, url2, options);
    }
}

function initViz3() {
    if (!viz3) {
        const vizContainer3 = document.getElementById('vizContainer3');
        viz3 = new tableau.Viz(vizContainer3, url3, options);
    }
}

// Load appropriate dashboard based on active tab
document.addEventListener("DOMContentLoaded", () => {
    document.getElementById("Dashboard1").addEventListener("click", initViz1);
    document.getElementById("Dashboard2").addEventListener("click", initViz2);
    document.getElementById("Dashboard3").addEventListener("click", initViz3);
});