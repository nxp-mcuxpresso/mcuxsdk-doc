(function () {
    var fallbackTooltip = null;

    function getTitle(link) {
        var title = link.getAttribute("title");
        if (title) {
            title = title.replace(/\\\//g, "/");
            link.dataset.titleTooltip = title;
            link.removeAttribute("title");
            return title;
        }
        return link.dataset.titleTooltip || "";
    }

    function showFallbackTooltip(link) {
        var title = getTitle(link);
        var rect;
        if (!title) {
            return;
        }

        if (!fallbackTooltip) {
            fallbackTooltip = document.createElement("div");
            fallbackTooltip.className = "title-tooltip-popup";
            fallbackTooltip.setAttribute("role", "tooltip");
            document.body.appendChild(fallbackTooltip);
        }

        fallbackTooltip.textContent = title;
        fallbackTooltip.classList.add("title-tooltip-popup-visible");
        rect = link.getBoundingClientRect();
        fallbackTooltip.style.left = Math.round(window.scrollX + rect.left) + "px";
        fallbackTooltip.style.top = Math.round(window.scrollY + rect.bottom + 6) + "px";
    }

    function hideFallbackTooltip() {
        if (fallbackTooltip) {
            fallbackTooltip.classList.remove("title-tooltip-popup-visible");
        }
    }

    function initTitleTooltips() {
        document.querySelectorAll('a[href="#"][title], a[href="#"][data-title-tooltip]').forEach(function (link) {
            getTitle(link);
            if (link.dataset.titleTooltipFallbackInitialized === "true") {
                return;
            }
            link.dataset.titleTooltipFallbackInitialized = "true";
            link.addEventListener("mouseenter", function () { showFallbackTooltip(link); });
            link.addEventListener("focus", function () { showFallbackTooltip(link); });
            link.addEventListener("mouseleave", hideFallbackTooltip);
            link.addEventListener("blur", hideFallbackTooltip);
        });
    }

    if (document.readyState === "complete") {
        initTitleTooltips();
    } else {
        window.addEventListener("load", initTitleTooltips);
    }
}());
