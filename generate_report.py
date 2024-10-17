import os
import shutil
import subprocess
import sys


def get_output(file_path):
    try:
        result = subprocess.run(
            ["python", file_path], capture_output=True, text=True, check=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        return e.output


def main():
    if len(sys.argv) != 2:
        print("Usage: python generate_report.py <directory>")
        sys.exit(1)

    directory = sys.argv[1]
    if not os.path.isdir(directory):
        print(f"Error: {directory} is not a valid directory")
        sys.exit(1)

    report = r"""\documentclass{article}
\usepackage{listings}
\usepackage{xcolor}
\usepackage{graphicx}
\lstset{
    language=Python,
    basicstyle=\ttfamily\small,
    keywordstyle=\color{blue},
    stringstyle=\color{red},
    commentstyle=\color{green},
    frame=single,
    showstringspaces=false,
    breaklines=true,
    numbers=left,
    numberstyle=\tiny,
    numbersep=5pt,
    tabsize=4
}

\begin{document}

\begin{titlepage}
    \centering
    \includegraphics[width=0.3\textwidth]{asufe.png} \\[1cm]
    {\scshape\LARGE Lab 1 \par}
    \vspace{1.5cm}
    {\scshape\large Section 1 (CSE) \par}
    \vspace{1.5cm}
    {\scshape\Large System Dynamics and Control Components \par}
    \vspace{2cm}
    {\scshape\Huge Khalid Alansary \par}
    {\scshape\Medium 2100259 \par}
    \vfill
\end{titlepage}
"""
    for filename in sorted(os.listdir(directory)):
        if filename.endswith(".py"):
            question = filename[1:-3].replace("_", "")
            print(f"Generating report for Question {question}")
            filepath = os.path.join(directory, filename)

            report += f"\\section*{{Question {question}}}\n"
            report += r"""\textbf{Python Code:}
\begin{lstlisting}
"""
            with open(filepath, encoding="utf-8") as f:
                report += f.read()
            report += r"\end{lstlisting}"
            report += r"""
\textbf{Terminal Output:}
\begin{lstlisting}
"""
            report += get_output(filepath).replace("─", r"_")
            report += r"\end{lstlisting}"
            report += r"\newpage"
    report += r"\end{document}"

    if not os.path.exists(os.path.join("reports", directory)):
        os.makedirs(os.path.join("reports", directory))
    # Create a {directory}.tex file
    with open(
        os.path.join("reports", directory, f"{directory}.tex"), "w", encoding="utf-8"
    ) as f:
        f.write(report)

    print(
        f"Latex file generated successfully at {os.path.join('reports', directory, directory)}.tex"
    )

    shutil.copy("asufe.png", os.path.join("reports", directory))

    try:
        subprocess.run(
            ["pdflatex", f"{directory}.tex"],
            cwd=os.path.join("reports", directory),
            check=True,
        )
        print(
            f"PDF generated successfully at {os.path.join('reports', directory, directory)}.pdf"
        )
    except subprocess.CalledProcessError as e:
        print(e.output)
    finally:
        os.remove(os.path.join("reports", directory, f"{directory}.aux"))
        os.remove(os.path.join("reports", directory, f"{directory}.log"))
        os.remove(os.path.join("reports", directory, "asufe.png"))


if __name__ == "__main__":
    main()
