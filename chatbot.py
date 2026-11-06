#!/usr/bin/env python3

import json
import re
from pathlib import Path

EXIT_COMMANDS = {"bye", "exit", "quit"}


def load_faq(path="sample_faq.json"):
    file_path = Path(path)
    if not file_path.exists():
        return {
            "business_hours": [
                "Our business hours are Monday to Friday, 9:00 AM to 6:00 PM.",
                "We are closed on weekends and public holidays."
            ],
            "shipping": [
                "Standard shipping takes 3-5 business days.",
                "Express shipping is available for urgent orders."
            ],
            "returns": [
                "Returns are accepted within 30 days of purchase.",
                "Items must be in original condition for a refund or exchange."
            ],
            "support": [
                "Our support team can help with order issues, product questions, and troubleshooting.",
                "You can contact us via email at support@example.com."
            ],
            "pricing": [
                "Pricing varies by product and promotion.",
                "Check the product page or contact sales for a custom quote."
            ],
        }

    with file_path.open("r", encoding="utf-8") as file:
        data = json.load(file)

    if isinstance(data, dict):
        return data
    return {}


def normalize_text(text):
    return re.sub(r"\s+", " ", text.strip().lower())


def contains_any(text, keywords):
    return any(keyword in text for keyword in keywords)


def get_intent(user_input, faq_data):
    text = normalize_text(user_input)

    if text in EXIT_COMMANDS:
        return "exit"

    greeting_patterns = [r"\bhi\b", r"\bhello\b", r"\bhey\b", r"\bgood morning\b", r"\bgood afternoon\b"]
    if any(re.search(pattern, text) for pattern in greeting_patterns):
        return "greeting"

    business_keywords = ["hours", "open", "closed", "business hours", "working time", "operating hours"]
    if contains_any(text, business_keywords):
        return "business_hours"

    shipping_keywords = ["shipping", "delivery", "order status", "track order", "where is my package"]
    if contains_any(text, shipping_keywords):
        return "shipping"

    return_policy_keywords = ["return", "refund", "exchange", "cancel order"]
    if contains_any(text, return_policy_keywords):
        return "returns"

    support_keywords = ["support", "help", "problem", "issue", "troubleshoot", "bug"]
    if contains_any(text, support_keywords):
        return "support"

    pricing_keywords = ["price", "cost", "quote", "pricing", "how much", "discount"]
    if contains_any(text, pricing_keywords):
        return "pricing"

    if "thank" in text:
        return "thanks"

    return "unknown"


def build_response(intent, faq_data):
    responses = {
        "greeting": "Hello! I can help with business hours, shipping, returns, product support, and pricing.",
        "business_hours": faq_data.get("business_hours", ["Our business hours are Monday to Friday, 9 AM to 6 PM."])[0],
        "shipping": faq_data.get("shipping", ["Shipping usually takes 3-5 business days."])[0],
        "returns": faq_data.get("returns", ["Returns are accepted within 30 days of purchase."])[0],
        "support": faq_data.get("support", ["Please contact support@example.com for help."])[0],
        "pricing": faq_data.get("pricing", ["Please visit the product page or contact sales for pricing details."])[0],
        "thanks": "You’re welcome! Let me know if you need anything else.",
        "exit": "Goodbye! Have a great day.",
    }

    return responses.get(intent, "I'm not sure how to help with that. Please ask about business hours, shipping, returns, support, or pricing.")


def chatbot():
    faq_data = load_faq()
    print("Customer Support Assistant")
    print("Type 'exit', 'quit', or 'bye' to end the conversation.\n")

    while True:
        try:
            user_input = input("You: ").strip()
        except EOFError:
            print("\nSession ended.")
            break

        if not user_input:
            print("Please type a question or command.")
            continue

        intent = get_intent(user_input, faq_data)
        if intent == "exit":
            print(build_response(intent, faq_data))
            break

        response = build_response(intent, faq_data)
        print(f"Bot: {response}\n")


if __name__ == "__main__":
    chatbot()
