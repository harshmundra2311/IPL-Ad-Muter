# IPL Ad Muter using Logo Detection

This Python script automatically **mutes or unmutes your system audio during IPL matches** by detecting the IPL logo in a specific screen region. It is built using **OpenCV**, **MSS**, and **pycaw**, and is tailored for Windows.

## How It Works

- The script continuously captures a small region of your screen using `mss`.
- It uses OpenCV's template matching to check for the presence of the IPL logo (`ipl_logo.jpg`).
- If the IPL logo is found: **audio is unmuted**.
- If not (likely during ads): **audio is muted**.
- This allows you to enjoy the match while avoiding repetitive or irrelevant ads.

## Features

- Real-time logo detection
- Automatic mute/unmute control
- Lightweight and non-intrusive

## Known Issue

Currently, during transitions where the IPL logo briefly switches to a **home team logo or another visual**, the script may mistakenly **mute the audio**. This is because the IPL logo disappears momentarily, triggering the mute function.

**Planned Improvement:**
- Add tolerance to brief logo disappearances (e.g., ignore logo absence for 1–2 seconds).
- Optionally detect multiple logos or use smarter image tracking.
- Optimize for lower CPU usage to allow smoother background performance.

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/ipl-ad-muter.git
    cd ipl-ad-muter
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Make sure your IPL logo image (`ipl_logo.jpg`) is present and update its path in the script:
    ```python
    template = cv2.imread(r'path_to_your_logo\ipl_logo.jpg', 0)
    ```

## How to Run

```bash
python main.py

---

Let me know if you'd like help modifying the code to handle brief logo disappearance or background optimization next.