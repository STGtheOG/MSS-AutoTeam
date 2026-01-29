# MSS Tools Launcher
# Main application that provides access to Auto Team and Stats Editor

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class MSSToolsLauncher:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("MSS Tools")
        self.root.resizable(False, False)

        # Track child windows
        self.autoteam_app = None
        self.statseditor_process = None

        self.setup_ui()

    def setup_ui(self):
        # Main frame with padding
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky="nsew")

        # Title
        title_label = ttk.Label(
            main_frame, text="MSS Tools", font=("Arial", 18, "bold")
        )
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))

        # Description
        desc_label = ttk.Label(
            main_frame, text="Select a tool to open:", font=("Arial", 10)
        )
        desc_label.grid(row=1, column=0, columnspan=2, pady=(0, 15))

        # Auto Team button
        autoteam_btn = ttk.Button(
            main_frame, text="Auto Team", command=self.open_autoteam, width=20
        )
        autoteam_btn.grid(row=2, column=0, padx=10, pady=10)

        # Auto Team description
        autoteam_desc = ttk.Label(
            main_frame,
            text="Create and manage teams\nfor Mario Super Sluggers",
            font=("Arial", 9),
            justify="center",
        )
        autoteam_desc.grid(row=3, column=0, padx=10)

        # Stats Editor button
        statseditor_btn = ttk.Button(
            main_frame, text="Stats Editor", command=self.open_statseditor, width=20
        )
        statseditor_btn.grid(row=2, column=1, padx=10, pady=10)

        # Stats Editor description
        statseditor_desc = ttk.Label(
            main_frame,
            text="Edit character stats,\nchemistry, and more",
            font=("Arial", 9),
            justify="center",
        )
        statseditor_desc.grid(row=3, column=1, padx=10)

        # Footer
        footer_label = ttk.Label(
            main_frame,
            text="Programmed by STG, with help from Whodeyy, Kircher, Harrhy\nand the rest of the MSS community",
            font=("Arial", 8),
            justify="center",
        )
        footer_label.grid(row=4, column=0, columnspan=2, pady=(20, 0))

    def open_autoteam(self):
        """Open the Auto Team application window."""
        # Check if already open
        if self.autoteam_app is not None:
            try:
                self.autoteam_app.master.lift()
                self.autoteam_app.master.focus_force()
                return
            except tk.TclError:
                # Window was closed
                self.autoteam_app = None

        # Import and create the AutoTeam app
        try:
            from autoteam import AutoTeamApp

            self.autoteam_app = AutoTeamApp(self.root)
        except ImportError as e:
            messagebox.showerror("Error", f"Could not load Auto Team module: {e}")

    def open_statseditor(self):
        """Open the Stats Editor application window."""
        import subprocess
        import sys
        import os

        # Run as separate process since module has module-level UI code
        editor_path = os.path.join(os.path.dirname(__file__), "statseditor.py")
        subprocess.Popen([sys.executable, editor_path])

    def run(self):
        """Start the main event loop."""
        self.root.mainloop()


def main():
    app = MSSToolsLauncher()
    app.run()


if __name__ == "__main__":
    main()
