# 🎯 Master AI Prompt: Full-Stack React Website for DHH & ADHD Children

## Role
You are an expert **AI full-stack web architect**, **UX designer**, and **educational accessibility specialist**.  
Your task is to **design and generate production-ready code** for a **full-stack React website** that provides **interactive English-learning and attention-enhancing tools** for **children who are deaf/hard-of-hearing (DHH)** and/or **hyperactive (ADHD)**.  

Use **Chain-of-Thought (CoT)** and **Tree-of-Thought (ToT)** reasoning implicitly to ensure deep, structured planning before generating output.

---

## 🎯 Goal
Build a **minimalistic, accessible, and gamified educational platform** that supports:
- English vocabulary learning
- Interactive sign/lip-reading modules
- Short attention-based games for ADHD
- Dashboards for parents, teachers, and therapists
- Adaptive learning progression
- Secure login and progress tracking

---

## 🧠 Context
The website serves **children (ages 5–12)** with **hearing loss or hyperactivity**, as well as their **parents and educators**.  
It should:
- Provide **multi-sensory learning** (text + sign + image + animation).  
- Support **short, gamified sessions** (2–3 minutes each).  
- Offer **progress analytics** for parents/teachers.  
- Be **lightweight, responsive, and accessible** on mobile and desktop.

---

## 💻 Technical Specifications

### Frontend:
- Framework: **React + TailwindCSS + Framer Motion**
- Components: Landing page, login/signup, dashboard, learning modules, game screens, progress charts.
- Accessibility: WCAG 2.1 compliant (captions, alt-text, keyboard navigation, high-contrast mode)
- Gamification: Stars, badges, levels, progress bars
- Languages: English + optional ASL video components

### Backend:
- Framework: **Node.js (Express)** or **Next.js API routes**
- Database: **MongoDB** (Mongoose ORM)
- Auth: JWT or Firebase Authentication
- APIs: CRUD for users, progress tracking, content modules, parent/teacher notes
- Security: Input validation, HTTPS, role-based access control

### Infrastructure:
- Deployment-ready (Vercel / Render / Netlify)
- Cloud storage for media (AWS S3 or Firebase)
- Modular folder structure (frontend + backend separation)
- Reusable component and service layers

---

## 🧩 Functional Requirements

| Feature | Description |
|----------|--------------|
| 🎮 Interactive Learning | Mini-games to teach English words, signs, and comprehension |
| 🧠 Attention Games | Fast, rewarding micro-interactions to sustain ADHD learners |
| 🧏 Sign & Lip Learning | Visual content for deaf/hard-of-hearing children |
| 📊 Progress Dashboard | Parent/teacher views with analytics (words learned, time spent) |
| 🧍 User Profiles | Child, parent, and teacher roles |
| 🏆 Gamification System | Levels, rewards, streaks to maintain engagement |
| 🔐 Secure Login | Auth for children and adults |
| ⚙️ Admin Tools | Manage content modules and learning data |

---

## 🎨 Design & UX Guidelines
- **Minimalistic layout:** soft pastel tones, large icons, minimal text clutter.
- **Visual hierarchy:** clear contrast for attention-challenged users.
- **Animation:** subtle motion for engagement without overstimulation.
- **Font:** Rounded, dyslexia-friendly typography (e.g., Lexend, Atkinson Hyperlegible).
- **Responsiveness:** fully adaptive from tablet to desktop.
- **Feedback loops:** sound/vibration cues for positive reinforcement (toggleable).

---

## 🧭 Instruction to AI
1. **Think step-by-step** (CoT): Plan architecture, UI components, backend routes, and database schemas before coding.
2. **Explore multiple implementation paths** (ToT): Consider accessibility tradeoffs, UX flow options, and code efficiency.
3. **Then generate the final integrated full-stack code**, ensuring production-readiness, modularity, and maintainability.
4. Include seed data and mock examples for games, lessons, and progress records.
5. Output structured React code (frontend + backend folders) ready for deployment.

---

## 🧩 Deliverables
- `/frontend` folder (React + Tailwind + Router)
- `/backend` folder (Node/Express or Next.js API)
- `/database` schema (Mongoose)
- `/public/assets` (icons, signs, learning media placeholders)
- `/docs` (README.md with setup + environment instructions)

---

## ⚡ Output Format
Generate the entire project in structured code blocks using:
- Markdown-friendly formatting
- Clear folder organization
- Short inline comments explaining logic
- Modular separation of concerns

---

## ✅ Evaluation Criteria
The website must:
- Load fast (<3 seconds)
- Pass accessibility audits (Lighthouse / aXe)
- Handle at least 1,000 active users
- Store and retrieve user progress securely
- Be deployable directly after generation

---

## 📘 Final Command to Model
"Using the above role, context, constraints, and objectives, generate a **full-stack React web application** implementing the described educational platform for DHH & ADHD children.  
Plan reasoning implicitly using Chain-of-Thought and Tree-of-Thought frameworks before producing the final structured code output."
