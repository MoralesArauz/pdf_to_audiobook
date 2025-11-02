import boto3
import pdfplumber
import os

# --- Step 1: Extract text from PDF ---
def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text

# --- Step 2: Chunk long text for Polly (max ~3000 chars per request) ---
def chunk_text(text, max_length=2900):
    chunks = []
    while len(text) > max_length:
        split_at = text.rfind('.', 0, max_length) + 1
        if split_at == 0:
            split_at = max_length
        chunks.append(text[:split_at].strip())
        text = text[split_at:].strip()
    if text:
        chunks.append(text)
    return chunks

# --- Step 3: Synthesize each chunk with Polly ---
# Using default voice "Joanna" and region "us-east-1"
# - Try other voices like "Matthew", "Lupe" (Spanish), or "Amy".
def synthesize_with_polly(text, output_path, voice_id="Joanna", region="us-east-1"):
    polly = boto3.client("polly", region_name=region)
    response = polly.synthesize_speech(
        Text=text,
        OutputFormat="mp3",
        VoiceId=voice_id
    )
    with open(output_path, "wb") as f:
        f.write(response["AudioStream"].read())
    print(f"✅ Saved: {output_path}")

# --- Step 4: Combine everything ---
def pdf_to_audiobook(pdf_path, output_dir="audiobook", voice="Joanna"):
    os.makedirs(output_dir, exist_ok=True)
    full_text = extract_text_from_pdf(pdf_path)
    chunks = chunk_text(full_text)

    for i, chunk in enumerate(chunks):
        filename = os.path.join(output_dir, f"part_{i+1}.mp3")
        synthesize_with_polly(chunk, filename, voice_id=voice)

    print(f"\n🎧 Done! {len(chunks)} audio files saved in '{output_dir}'.")

# --- Run it ---
if __name__ == "__main__":
    pdf_file = "for_whom_the_bells_tolls.pdf"  # Replace with your PDF filename
    pdf_to_audiobook(pdf_file)