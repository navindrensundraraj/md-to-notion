---
title: "Free Live Sports Setup"
date: 2024-07-27
tags: [chatgpt, export]
---

# Free Live Sports Setup

---
**User:**

Best live tv free setup for sports in jellyfin

---
**Assistant:**

The user is interested in setting up live TV for sports on Jellyfin.

---
**Tool:**

Model set context updated.

---
**Assistant:**

To set up the best live TV experience for sports in Jellyfin for free, follow these steps:

### 1. Install Jellyfin
- Ensure you have Jellyfin installed on your server. You can download it from the [Jellyfin website](https://jellyfin.org/downloads/).

### 2. Set Up a TV Tuner (Optional)
- If you have a TV tuner, you can integrate it with Jellyfin to stream live TV channels. This might require additional hardware like an HDHomeRun tuner.

### 3. Configure IPTV
- **Find Free IPTV Sources**: You can find free IPTV sources from various websites. Some popular ones include:
  - [IPTV-org](https://iptv-org.github.io/)
  - [Free-IPTV](https://github.com/Free-IPTV/Countries)
  - [Fluxus IPTV](https://www.fluxustv.com/)
- **Add IPTV to Jellyfin**:
  1. Open Jellyfin and navigate to **Live TV** in the admin dashboard.
  2. Click on **Add Tuner Device**.
  3. Select **IPTV** and enter the M3U URL you got from the free IPTV source.
  4. Click **Save**.

### 4. Set Up EPG (Electronic Program Guide)
- **Find EPG Sources**: Many IPTV sources provide EPG data. You can also find EPG data from sources like [XMLTV](http://xmltv.org/) or other websites.
- **Add EPG to Jellyfin**:
  1. Navigate to **Live TV** in the admin dashboard.
  2. Click on **Add Guide Data Provider**.
  3. Select **XMLTV** and enter the EPG URL.
  4. Click **Save**.

### 5. Optimize for Sports
- **Channel Sorting**: Ensure that your favorite sports channels are easily accessible by organizing them at the top of your channel list.
- **Favorites**: Mark your favorite sports channels so you can quickly access them.

### 6. Mobile and Remote Access
- **Jellyfin App**: Download the Jellyfin app on your mobile device to watch live sports on the go.
- **Port Forwarding**: Set up port forwarding on your router to access Jellyfin outside your local network if needed.

By following these steps, you can enjoy a robust live TV setup for sports in Jellyfin without any subscription fees.

---
**User:**

Can u give a free Sports iptv link

---
**Assistant:**

Here is a free sports IPTV link from a reliable source:

- [IPTV-org Sports M3U](https://iptv-org.github.io/iptv/index.m3u)

This M3U link includes a variety of sports channels from around the world. To use it in Jellyfin:

1. Open Jellyfin and navigate to **Live TV** in the admin dashboard.
2. Click on **Add Tuner Device**.
3. Select **IPTV** and enter the M3U URL above.
4. Click **Save**.

This should set up a range of sports channels for you to enjoy.

---
**User:**

Can u give an epg for this

---
**Assistant:**

For EPG (Electronic Program Guide) data, you can use the following XMLTV link which is compatible with the IPTV-org sports channels:

- [IPTV-org EPG XMLTV](https://iptv-org.github.io/epg/guides.xml)

To integrate this EPG with Jellyfin:

1. Open Jellyfin and navigate to **Live TV** in the admin dashboard.
2. Click on **Add Guide Data Provider**.
3. Select **XMLTV**.
4. Enter the EPG URL above.
5. Click **Save**.

This will provide you with the program guide data for the sports channels available in the IPTV-org M3U link.
