"""
BITCOIN RECHNER - Desktop App with Glow Effects
Created for Michael - NodeWatch21 Builder
Bitcoin-Orange Glow Theme 🔥
"""

import customtkinter as ctk
import requests
from typing import Optional
import threading
import time
from datetime import datetime

# ===== CONFIGURATION =====
BITCOIN_ORANGE = "#f2a900"
DARK_BG = "#0a0a0a"
CARD_BG = "#1a1a1a"
TEXT_COLOR = "#ffffff"
GLOW_COLOR = "#f2a900"

# ===== BITCOIN PRICE API =====
class BitcoinPriceAPI:
    def __init__(self):
        self.price_eur = 0.0
        self.last_update = None
        self.running = True
        
    def get_price(self) -> Optional[float]:
        """Fetch current Bitcoin price in EUR from CoinGecko"""
        try:
            response = requests.get(
                "https://api.coingecko.com/api/v3/simple/price",
                params={"ids": "bitcoin", "vs_currencies": "eur"},
                timeout=5
            )
            if response.status_code == 200:
                data = response.json()
                self.price_eur = data["bitcoin"]["eur"]
                self.last_update = datetime.now()
                return self.price_eur
        except Exception as e:
            print(f"Error fetching price: {e}")
        return None
    
    def start_auto_update(self, callback):
        """Start background thread for price updates"""
        def update_loop():
            while self.running:
                price = self.get_price()
                if price and callback:
                    callback(price)
                time.sleep(30)  # Update every 30 seconds
        
        thread = threading.Thread(target=update_loop, daemon=True)
        thread.start()
    
    def stop(self):
        self.running = False


# ===== MAIN APPLICATION =====
class BitcoinRechner(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Window setup
        self.title("₿ Bitcoin Calc")
        self.geometry("500x800")  # Increased height for all results to be visible
        self.resizable(False, False)
        
        # Set theme
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        # Initialize API
        self.api = BitcoinPriceAPI()
        self.btc_price = 0.0
        
        # Lightning pulse animation variables
        self.title_symbols = ["₿", "⚡"]
        self.current_symbol_index = 0
        self.symbol_show_time = 1500  # Show ₿ for 1.5 seconds
        self.lightning_show_time = 500  # Show ⚡ for 0.5 seconds
        
        # Setup UI
        self.setup_ui()
        
        # Fetch initial price
        self.update_price_display()
        
        # Start auto-updates
        self.api.start_auto_update(self.on_price_update)
        
        # Start title animation
        self.animate_title()
    
    def setup_ui(self):
        """Create the user interface"""
        
        # Main container
        self.configure(fg_color=DARK_BG)
        
        # ===== HEADER =====
        header_frame = ctk.CTkFrame(self, fg_color=DARK_BG, corner_radius=0)
        header_frame.pack(fill="x", padx=20, pady=(20, 10))
        
        # Animated header label with Lightning pulse
        self.title_label = ctk.CTkLabel(
            header_frame,
            text="₿ BITCOIN CALC",
            font=ctk.CTkFont(size=28, weight="bold"),
            text_color=BITCOIN_ORANGE
        )
        self.title_label.pack()
        
        # ===== PRICE DISPLAY =====
        self.price_frame = ctk.CTkFrame(
            self,
            fg_color=CARD_BG,
            corner_radius=15,
            border_width=2,
            border_color=BITCOIN_ORANGE
        )
        self.price_frame.pack(fill="x", padx=20, pady=10)
        
        self.price_label = ctk.CTkLabel(
            self.price_frame,
            text="Loading...",
            font=ctk.CTkFont(size=24, weight="bold"),
            text_color=BITCOIN_ORANGE
        )
        self.price_label.pack(pady=15)
        
        self.update_label = ctk.CTkLabel(
            self.price_frame,
            text="",
            font=ctk.CTkFont(size=11),
            text_color="#888888"
        )
        self.update_label.pack(pady=(0, 10))
        
        # ===== CONVERTER SECTIONS =====
        
        # EUR Section
        self.create_converter_section(
            "EURO",
            "eur",
            "EUR",
            self.on_eur_change
        )
        
        # SATS Section (moved to second position)
        self.create_converter_section(
            "SATOSHIS",
            "sats",
            "SATS",
            self.on_sats_change
        )
        
        # BTC Section (moved to third position)
        self.create_converter_section(
            "BITCOIN",
            "btc",
            "BTC",
            self.on_btc_change
        )
        
        # ===== FOOTER =====
        footer_frame = ctk.CTkFrame(self, fg_color=DARK_BG, corner_radius=0)
        footer_frame.pack(fill="x", padx=20, pady=20)
        
        footer_label = ctk.CTkLabel(
            footer_frame,
            text="Made with ₿ by Michael | NodeWatch21",
            font=ctk.CTkFont(size=11),
            text_color="#666666"
        )
        footer_label.pack()
    
    def create_converter_section(self, title, key, unit, callback):
        """Create a converter section with input and results"""
        
        section_frame = ctk.CTkFrame(
            self,
            fg_color=CARD_BG,
            corner_radius=15,
            border_width=1,
            border_color="#333333"
        )
        section_frame.pack(fill="x", padx=20, pady=10)
        
        # Title
        title_label = ctk.CTkLabel(
            section_frame,
            text=title,
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color=BITCOIN_ORANGE
        )
        title_label.pack(pady=(15, 5))
        
        # Input
        input_frame = ctk.CTkFrame(section_frame, fg_color=CARD_BG)
        input_frame.pack(fill="x", padx=20, pady=5)
        
        entry = ctk.CTkEntry(
            input_frame,
            placeholder_text=f"Enter {unit}",
            font=ctk.CTkFont(size=16),
            height=40,
            fg_color="#2a2a2a",
            border_color=BITCOIN_ORANGE,
            border_width=2,
            text_color=TEXT_COLOR
        )
        entry.pack(side="left", fill="x", expand=True, padx=(0, 10))
        
        unit_label = ctk.CTkLabel(
            input_frame,
            text=unit,
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color=BITCOIN_ORANGE,
            width=60
        )
        unit_label.pack(side="right")
        
        # Results
        result1_label = ctk.CTkLabel(
            section_frame,
            text="",
            font=ctk.CTkFont(size=14),
            text_color="#aaaaaa"
        )
        result1_label.pack(pady=2)
        
        result2_label = ctk.CTkLabel(
            section_frame,
            text="",
            font=ctk.CTkFont(size=14),
            text_color="#aaaaaa"
        )
        result2_label.pack(pady=(2, 15))
        
        # Store references
        setattr(self, f"{key}_entry", entry)
        setattr(self, f"{key}_result1", result1_label)
        setattr(self, f"{key}_result2", result2_label)
        
        # Bind callback
        entry.bind("<KeyRelease>", callback)
    
    def update_price_display(self):
        """Fetch and display current Bitcoin price"""
        price = self.api.get_price()
        if price:
            self.btc_price = price
            self.price_label.configure(
                text=f"₿ {price:,.2f} EUR"
            )
            if self.api.last_update:
                time_str = self.api.last_update.strftime("%H:%M:%S")
                self.update_label.configure(
                    text=f"Last Update: {time_str}"
                )
    
    def on_price_update(self, price):
        """Callback for price updates from background thread"""
        self.btc_price = price
        self.price_label.configure(
            text=f"₿ {price:,.2f} EUR"
        )
        if self.api.last_update:
            time_str = self.api.last_update.strftime("%H:%M:%S")
            self.update_label.configure(
                text=f"Last Update: {time_str}"
            )
    
    def on_eur_change(self, event=None):
        """Handle EUR input changes"""
        try:
            eur = float(self.eur_entry.get().replace(",", "."))
            if self.btc_price > 0:
                btc = eur / self.btc_price
                sats = btc * 100_000_000
                
                self.eur_result1.configure(
                    text=f"= {btc:.8f} BTC",
                    text_color=BITCOIN_ORANGE
                )
                self.eur_result2.configure(
                    text=f"= {sats:,.0f} SATS",
                    text_color=BITCOIN_ORANGE
                )
        except ValueError:
            self.eur_result1.configure(text="", text_color="#aaaaaa")
            self.eur_result2.configure(text="", text_color="#aaaaaa")
    
    def on_btc_change(self, event=None):
        """Handle BTC input changes"""
        try:
            btc = float(self.btc_entry.get().replace(",", "."))
            if self.btc_price > 0:
                eur = btc * self.btc_price
                sats = btc * 100_000_000
                
                self.btc_result1.configure(
                    text=f"= {eur:,.2f} EUR",
                    text_color=BITCOIN_ORANGE
                )
                self.btc_result2.configure(
                    text=f"= {sats:,.0f} SATS",
                    text_color=BITCOIN_ORANGE
                )
        except ValueError:
            self.btc_result1.configure(text="", text_color="#aaaaaa")
            self.btc_result2.configure(text="", text_color="#aaaaaa")
    
    def on_sats_change(self, event=None):
        """Handle SATS input changes"""
        try:
            sats = float(self.sats_entry.get().replace(",", ""))
            btc = sats / 100_000_000
            if self.btc_price > 0:
                eur = btc * self.btc_price
                
                self.sats_result1.configure(
                    text=f"= {eur:.8f} EUR",
                    text_color=BITCOIN_ORANGE
                )
                self.sats_result2.configure(
                    text=f"= {btc:.8f} BTC",
                    text_color=BITCOIN_ORANGE
                )
        except ValueError:
            self.sats_result1.configure(text="", text_color="#aaaaaa")
            self.sats_result2.configure(text="", text_color="#aaaaaa")
    
    def on_closing(self):
        """Clean shutdown"""
        self.api.stop()
        self.destroy()
    
    def animate_title(self):
        """Animate window title AND header with Bitcoin ⚡ Lightning pulse"""
        # Get current symbol
        symbol = self.title_symbols[self.current_symbol_index]
        
        # Update window title
        self.title(f"{symbol} Bitcoin Calc")
        
        # Update header label
        self.title_label.configure(text=f"{symbol} BITCOIN CALC")
        
        # Toggle to next symbol
        self.current_symbol_index = (self.current_symbol_index + 1) % len(self.title_symbols)
        
        # Determine next delay (₿ shows longer, ⚡ shows shorter)
        if symbol == "₿":
            delay = self.symbol_show_time  # 1.5 seconds for Bitcoin
        else:
            delay = self.lightning_show_time  # 0.5 seconds for Lightning
        
        # Schedule next update
        self.after(delay, self.animate_title)


# ===== MAIN ENTRY POINT =====
if __name__ == "__main__":
    app = BitcoinRechner()
    app.protocol("WM_DELETE_WINDOW", app.on_closing)
    app.mainloop()
