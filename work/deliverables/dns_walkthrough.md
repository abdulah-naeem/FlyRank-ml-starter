# DNS Walkthrough: How a Web Address Becomes a Real Website

**Author:** Abdullah Naeem  
**Date:** September 9, 2026

---

## What DNS Does

DNS stands for **Domain Name System**. It is the internet's phone book.

Computers communicate using IP addresses — strings of numbers like `104.26.10.78`. Humans prefer readable names like `abdullah-naeem.netlify.app`. DNS is the system that translates one into the other. Every time you type a website address into your browser, DNS is what figures out which server on the internet to actually talk to.

Without DNS, you would need to memorize the IP address of every website you want to visit.

---

## What a CNAME Record Is

A **CNAME** (Canonical Name) record is a type of DNS record that says: *"This domain name is actually an alias for another domain name."*

For example, if I buy the domain `abdullahnaeem.com` and want it to point to my Netlify-hosted site, I would create a CNAME record like:

```
abdullahnaeem.com  →  CNAME  →  abdullah-naeem.netlify.app
```

This tells the DNS system: "When someone looks up `abdullahnaeem.com`, don't return an IP address directly — instead, go look up `abdullah-naeem.netlify.app` and use whatever IP address *that* resolves to."

This is useful because hosting platforms like Netlify may change their server IP addresses over time. With a CNAME, your custom domain always follows wherever Netlify points, without you needing to update anything.

---

## The Full Journey: From Typing a URL to Seeing a Website

Here is what actually happens, step by step, when someone types `abdullah-naeem.netlify.app` into their browser and presses Enter:

### Step 1: Browser Cache Check
The browser first checks its own memory: *"Have I looked up this domain recently?"* If it has a cached answer from the last few minutes, it skips straight to connecting. If not, it moves on.

### Step 2: Operating System Cache
The browser asks the operating system (Windows, macOS, etc.): *"Do you know the IP address for this domain?"* The OS checks its own DNS cache. If it finds a recent answer, it returns it. If not, it asks the network.

### Step 3: Recursive Resolver
The request goes to a **recursive resolver** — a DNS server usually operated by your internet provider (ISP) or a public service like Cloudflare (`1.1.1.1`) or Google (`8.8.8.8`). This resolver's job is to track down the answer by asking other servers on your behalf.

Think of the recursive resolver as a librarian: you ask a question, and the librarian goes shelf by shelf until they find the answer.

### Step 4: Root Nameserver
The resolver starts at the top. It asks one of the 13 **root nameservers** (the very top of the DNS hierarchy): *"Who is responsible for `.app` domains?"*

The root server doesn't know the final answer, but it says: *"Go ask the `.app` TLD nameserver at this address."*

### Step 5: TLD Nameserver
The resolver follows the referral and asks the **TLD (Top-Level Domain) nameserver** for `.app`: *"Who is responsible for `netlify.app`?"*

The TLD server responds: *"The authoritative nameserver for `netlify.app` is at this address."*

### Step 6: Authoritative Nameserver
The resolver asks Netlify's **authoritative nameserver**: *"What is the IP address for `abdullah-naeem.netlify.app`?"*

This is the server that actually holds the definitive record. It replies with an answer — for example:

```
abdullah-naeem.netlify.app  →  A Record  →  104.26.10.78
```

### Step 7: Response Delivered
The recursive resolver sends this IP address back to your browser. The resolver also caches the answer for a set amount of time (called the **TTL** — Time to Live), so future lookups are faster.

### Step 8: HTTPS Connection
Your browser now has the IP address. It connects to `104.26.10.78` and initiates a **TLS handshake** (the "S" in HTTPS). This establishes an encrypted connection, verifying that the server is who it claims to be using an SSL certificate. Netlify provides this certificate automatically for free.

### Step 9: The Page Loads
The server sends back the HTML, CSS, and assets for the website. Your browser renders them on screen. The entire process — from typing the URL to seeing the page — typically takes under 200 milliseconds.

---

## Visual Summary

```
You type: abdullah-naeem.netlify.app
              │
              ▼
    ┌─────────────────┐
    │  Browser Cache   │ ── cached? → use it
    └────────┬────────┘
             ▼
    ┌─────────────────┐
    │    OS Cache      │ ── cached? → use it
    └────────┬────────┘
             ▼
    ┌─────────────────┐
    │Recursive Resolver│ (ISP / Cloudflare / Google)
    └────────┬────────┘
             ▼
    ┌─────────────────┐
    │ Root Nameserver  │ → "Ask the .app TLD server"
    └────────┬────────┘
             ▼
    ┌─────────────────┐
    │ .app TLD Server  │ → "Ask Netlify's nameserver"
    └────────┬────────┘
             ▼
    ┌─────────────────┐
    │  Authoritative   │ → "IP is 104.26.10.78"
    │  Nameserver      │
    └────────┬────────┘
             ▼
    ┌─────────────────┐
    │  HTTPS / TLS     │ → Encrypted connection established
    └────────┬────────┘
             ▼
        Page loads ✅
```

---

## Key Terms (Quick Reference)

| Term | What It Means |
|---|---|
| **DNS** | Domain Name System — translates domain names to IP addresses |
| **A Record** | Maps a domain directly to an IP address |
| **CNAME Record** | Maps a domain to another domain (an alias) |
| **Recursive Resolver** | The server that does the lookup work on your behalf |
| **Root Nameserver** | The top of the DNS hierarchy; directs to TLD servers |
| **TLD Nameserver** | Manages a top-level domain (.com, .app, .org, etc.) |
| **Authoritative Nameserver** | The server that holds the actual, definitive DNS records |
| **TTL** | Time to Live — how long a DNS answer is cached before re-checking |
| **TLS / HTTPS** | Encryption layer that secures the connection after DNS resolves |
