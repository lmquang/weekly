.PHONY: install build deploy all clean deploy-if-configured

# Default target
all: build deploy-if-configured

# Install dependencies
install:
	npm install

# Build the project (output will be in ./dist)
build:
	npm run build

# Deploy to Cloudflare Pages
# Note: Ensure you are logged in via 'npx wrangler login'
deploy:
	rm -rf .wrangler/deploy
	npx wrangler pages deploy dist --project-name weekly

deploy-if-configured:
	@if [ -n "$$CLOUDFLARE_API_TOKEN" ]; then \
		$(MAKE) deploy; \
	else \
		printf '%s\n' 'Skipping deploy: set CLOUDFLARE_API_TOKEN to enable Cloudflare Pages deploy.'; \
	fi

dev:
	npm run dev

# Clean build artifacts
clean:
	rm -rf dist .wrangler/deploy
