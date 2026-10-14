import os

# Wrapper for story generation. Tries to use local GPT4All if available, otherwise falls back to a simple template generator.

def generate_story(idea: str, title: str = 'Story', max_tokens: int = 600) -> str:
    """Generate a story from an idea.

    Attempts to use gpt4all (if installed). If not available, creates a coherent story using a simple template.
    """
    # Try to import gpt4all dynamically so this repo doesn't strictly require it.
    try:
        from gpt4all import GPT4All
        model_name = os.environ.get('GPT4ALL_MODEL') or 'ggml-model.bin'
        # If model file doesn't exist, fall back
        if not os.path.exists(model_name):
            # Attempt default model loading (GPT4All may handle download paths)
            pass
        try:
            gptj = GPT4All(model_name)
            prompt = (
                f"You are a creative writer. Write a short audiobook-style narrative titled '{title}' "
                f"based on the following idea: {idea}\n\nStart the story now:\n"
            )
            resp = gptj.generate(prompt, max_tokens=max_tokens)
            # generate may return list or string depending on lib version
            if isinstance(resp, (list, tuple)):
                out = '\n'.join([str(r) for r in resp])
            else:
                out = str(resp)
            return out
        except Exception:
            # Fall through to fallback generator
            pass
    except Exception:
        # gpt4all not installed or failed
        pass

    # Simple fallback generator
    story_lines = []
    story_lines.append(f"{title}\n")
    story_lines.append(f"Based on idea: {idea}\n")
    story_lines.append("Once upon a time, there was a character who was driven by the idea above. They set out on an adventure that changed them forever.\n")
    story_lines.append("Along the way they met friends and faced challenges. The story focuses on growth, discovery, and a surprising twist.\n")
    story_lines.append("In the end, the character learns an unexpected truth and their world is different — but better.\n")

    # Repeat with small variations to reach approximate length
    out = '\n'.join(story_lines)
    while len(out.split()) < max_tokens * 0.75:
        out += '\n' + story_lines[2]
    return out
