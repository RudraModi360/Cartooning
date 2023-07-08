import filters
import flet
from flet import (
    ElevatedButton,
    FilePicker,
    FilePickerResultEvent,
    Page,
    Row,
    Text,
    icons,
)


def main(page: Page):

    img_url = 'C:\\Users\\Rudra\\Downloads\\project_logo.png'
    img = flet.Image(
        src=str(img_url),
        width=600,
        height=400,
        fit=flet.ImageFit.CONTAIN,
    )
    images = flet.Row(expand=1, wrap=False, scroll="always")
    page.update()
    page.add(img, images)
    # Pick files dialog
    file_path = []
    def pick_files_result(e: FilePickerResultEvent):
        global img_url
        selected_files.value = (
            ", ".join(map(lambda f: f.path, e.files)) if e.files else "Cancelled!"
        )
        path = e.path if e.path else "Cancelled!"

        file_path.insert(0, selected_files.value)
        img.src = file_path[0]
        page.update()
        print(file_path)
        selected_files.update()
        page.update()



    pick_files_dialog = FilePicker(on_result=pick_files_result)
    selected_files = Text()


    # Save file dialog
    def save_file_result(e: FilePickerResultEvent):
        filters.Filter_gray(file_path[0])
        save_file_path.value = e.path if e.path else "Cancelled!"
        print(save_file_path)
        save_file_path.update()

    save_file_dialog = FilePicker(on_result=save_file_result)
    save_file_path = Text()

    def bw(request):
        filters.Filter_gray(file_path[0])
    def cartoon(request):
        filters.cartoon(file_path[0])
    def anime(request):
        filters.cartoonize(file_path[0], 8)
    def removebg(request):
        filters.removebg(file_path[0])
    def sketch(request):
        filters.Edges(file_path[0])
    # hide all dialogs in overlay
    page.overlay.extend([pick_files_dialog, save_file_dialog])

    page.add(
        Row(
            [
                ElevatedButton(
                    "Pick files",
                    icon=icons.UPLOAD_FILE,
                    on_click=lambda _: pick_files_dialog.pick_files(
                        allow_multiple=False
                    ),
                ),
                selected_files,
            ]
        ),

        Row(
            [
                ElevatedButton("Anime Effect", on_click=anime),
                ElevatedButton("Sketch Effect", on_click=sketch),
                ElevatedButton("Black/White", on_click=bw),
                ElevatedButton("Cartoon Effect", on_click=cartoon),
                ElevatedButton("Remove Background", on_click=removebg)
            ]
        )

    )


flet.app(target=main)
