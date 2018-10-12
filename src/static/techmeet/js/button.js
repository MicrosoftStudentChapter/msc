/ Capture click events
button.addEventListener('click', function () {
    if (!completed) { // Don't do anything if downloading has been completed
        if (downloading) { // If it's downloading, stop the download
            stopDownload();
        } else { // Start the download
            startDownload();
        }
    }
});

// Start the download
function startDownload() {
    // Update variables and CSS classes
    downloading = true;
    buttonContainer.classList.add('downloading');
    animateIcon();
    // Update progress after 1s
    progressTimer = setTimeout(function () {
        buttonContainer.classList.add('progressing');
        animateProgress();
    }, 1000);
}

// Stop the download
function stopDownload() {
    // Update variables and CSS classes
    downloading = false;
    clearTimeout(progressTimer);
    buttonContainer.classList.remove('downloading');
    buttonContainer.classList.remove('progressing');
    // Stop progress and draw icons back to initial state
    stopProgress();
    iconLine.draw(0, '100%', 1, {easing: anime.easings['easeOutCubic']});
    iconSquare.draw('30%', '70%', 1, {easing: anime.easings['easeOutQuad']});
}



// Progress animation
function animateProgress() {
    // Fake progress animation from 0 to 100%
    // This should be replaced with real progress data (real progress percent instead '100%'), and maybe called multiple times
    circularProgressBar.draw(0, '100%', 2.5, {easing: anime.easings['easeInQuart'], update: updateProgress, callback: completedAnimation});
}


// Animation performed when download has been completed
function completedAnimation() {
    // Update variables and CSS classes
    completed = true;
    buttonContainer.classList.add('completed');
    // Wait 1s for the ball animation
    setTimeout(function () {
        button.classList.add('button-hidden');
        ball.classList.add('hidden');
        borderPath.classList.remove('hidden');
        // Morphing the path to the second shape
        var morph = anime({
            targets: borderPath,
            d: 'M 40 3.5 a 36.5 36.5 0 0 0 -36.5 36.5 a 36.5 36.5 0 0 0 10.5 26.5 C 35 86.5 90 91.5 120 91.5 S 205 86.5 226 66.5 a 36.5 36.5 0 0 0 10.5 -26.5 a 36.5 36.5 0 0 0 -36.5 -36.5 Z',
            duration: 100,
            easing: 'linear',
            complete: function () {
                // Morphing the path back to the original shape with elasticity
                morph = anime({
                    targets: borderPath,
                    d: 'M 40 3.5 a 36.5 36.5 0 0 0 -36.5 36.5 a 36.5 36.5 0 0 0 36.5 36.5 C 70 76.5 90 76.5 120 76.5 S 170 76.5 200 76.5 a 36.5 36.5 0 0 0 36.5 -36.5 a 36.5 36.5 0 0 0 -36.5 -36.5 Z',
                    duration: 1000,
                    elasticity: 600,
                    complete: function () {
                        // Update variables and CSS classes, and return the button to the original state
                        completed = false;
                        setTimeout(function () {
                            buttonContainer.classList.remove('completed');
                            button.classList.remove('button-hidden');
                            ball.classList.remove('hidden');
                            borderPath.classList.add('hidden');
                            stopDownload();
                        }, 500);
                    }
                });
            }
        });
    }, 1000);
}
