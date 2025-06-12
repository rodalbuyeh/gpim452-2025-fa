# GPIM 452 2025 Course Website

This repository contains the source code for the course website. The site is built with [Jekyll](https://jekyllrb.com) and uses the [Just the Docs](https://pmarsceill.github.io/just-the-docs/) theme.

## Recommended Development Workflow

### Option 1: Hybrid Workflow (Recommended)

**Best for:** Editing with AI assistance locally + reliable testing in the cloud

1. **Edit locally with Cursor/VS Code**
   - Make changes to course content, syllabus, etc.
   - Commit and push your changes to GitHub

2. **Test in GitHub Codespaces**
   - Go to your GitHub repository
   - Click **Code** → **Codespaces** → **Create codespace**
   - In the Codespace terminal:
   ```bash
   bundle install
   bundle exec jekyll serve --host 0.0.0.0
   ```
   - Codespaces will automatically forward port 4000
   - Click the popup to view your site in the browser

**Benefits:**
- No local dependency management headaches
- Always works in clean Linux environment
- Free tier available (120 core-hours/month)
- Easy port forwarding and sharing
- Best of both worlds: local editing + cloud testing

### Option 2: Local Development Environment

**⚠️ Apple Silicon (M1/M2/M3) Compatibility Issues**

If you're on Apple Silicon, you may encounter compilation issues with native gems like `eventmachine` and `nokogiri`. The hybrid workflow above is strongly recommended for Apple Silicon users.

**For other systems or if you want to try local development:**

1. Follow the GitHub documentation for [Setting up your GitHub Pages site locally with Jekyll](https://help.github.com/en/articles/setting-up-your-github-pages-site-locally-with-jekyll)

2. Install dependencies:
   ```bash
   bundle install
   ```

3. Start your local Jekyll server:
   ```bash
   bundle exec jekyll serve
   ```

4. Point your web browser to [http://localhost:4000](http://localhost:4000)

5. Reload your web browser after making a change to preview its effect

**Troubleshooting:**
- If you get an error about "webrick", run `bundle add webrick`
- If you encounter compilation errors on Apple Silicon, use the Codespaces workflow instead
- Delete `Gemfile.lock` and re-run `bundle install` if you encounter version conflicts

## Making Updates

1. Edit content files (`.md` files) locally
2. Test changes using one of the development workflows above
3. Commit and push to deploy to GitHub Pages

For more information about the theme, refer to [Just the Docs](https://pmarsceill.github.io/just-the-docs/).
