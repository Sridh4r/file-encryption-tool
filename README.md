# 🔐 Secret Keeper 2.0 - Your Personal Encryption Wizard

## 🌟 Welcome!
This isn't just another encryption tool - it's your digital diary lock, your message-in-a-bottle, and your file vault all in one. We've stripped away the nerdy complexity of encryption and made it simple enough for anyone to use.

**⚠️ Important Warning**: Secret Keeper 2.0 is for **fun and educational purposes only**. It uses a random 95-character substitution cipher, which is **not secure** for protecting sensitive or private data. This is not an industry-standard encryption method and should not be used for real-world security needs. For secure encryption, use established tools like VeraCrypt, Picocrypt, or GPG.

## 🆕 What's Cooking in This Kitchen?
- Got files to hide? Encrypt entire documents with ease!
- Traveling abroad? We speak all languages (UTF-8 support).
- Accident-prone? We've got your back with:
  - Key file protection
  - Overwrite warnings
  - Empty file checks

## 📦 What You're Getting
Your magical toolkit now contains these enchanted components:
1. `src/main.py` - The friendly command-line interface
2. `src/key_generation.py` - Your personal key forge
3. `src/encryption.py` - The cipher engine
4. `src/file_initializer.py` - Sets up your secure environment
5. `encryption_key.txt` - Your golden ticket (guard it like chocolate!)

## 🎩 How the Magic Works
Every letter in your message gets a secret identity:
- 'A' becomes '🍕'
- 'B' becomes '🚀'
- '1' becomes '🎁'
...and so on for all 95 printable ASCII characters! Your key file (`encryption_key.txt`) is the only map to reverse this character witness protection program. **Note**: The key is generated randomly but is not cryptographically secure, making it unsuitable for sensitive data.

## 🚪 Getting Started is a Breeze
1. Ensure you have Python 3.x installed.
2. Open your command line and type:
   ```
   python3 src/main.py
   ```

3. Pick your potion from the menu:
   - 1 - Lock a secret message
   - 2 - Unlock a coded message
   - 3 - Seal a file shut
   - 4 - Crack open a sealed file
   - 5 - Change your magic password

4. Follow the friendly prompts - no spellbook required!

## ⚠️ Safety Dance
❗ **Your `encryption_key.txt` is the ONE RING that rules them all.** Lose it, and your encrypted treasures are gone forever! While we protect it from accidental overwrites, it’s not encrypted itself and should be stored securely.

We've added training wheels:
- Key file is protected like grandma's china
- We'll double-check before overwriting files
- Empty files get a gentle warning

## 🧠 Wisdom from the Encryption Elders
1. Test drive your encryption immediately to ensure it works as expected.
2. Name encrypted files clearly, like `tax_secrets.encrypted`.
3. Backup your key in 2 places (cloud + USB is ideal).
4. Change your key occasionally, like toothbrushes, for fun.

## 🔧 Under the Hood (For Tech Wizards)
- Speaks UTF-8 like a native
- Uses a 95-character substitution cipher (for fun, not security)
- Error handling that actually helps
- Keys that remember themselves
- Modular design in `src` directory for easy maintenance and upgrades

## 📅 Freshly Baked on August 2025