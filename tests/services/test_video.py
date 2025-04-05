from moviepy import VideoFileClip

from app.services.video import make_video_title


def test_make_video_title():
    video_path = 'D:\github\MoneyPrinterTurbo\storage\\tasks\\task_id\combined-1.mp4'
    font_path = 'D:\github\MoneyPrinterTurbo\\resource\\fonts\MicrosoftYaHeiBold.ttc'
    video_clip = VideoFileClip(video_path)

    video_clip = make_video_title(video_clip, '小鵬汽车深度分析', font_path, 80)
    video_clip.write_videofile(
        "D:\github\MoneyPrinterTurbo\storage\\tasks\\task_id\\test.mp4",
        audio_codec="aac",  # 音频编码
        threads=4,
        logger=None,
    )

def test_video():
    """
    {
    "video_subject": "",
    "video_script": "最近小鹏汽车表现相当炸裂，市值突破1500亿，股价从今年1月份开始到现在接近翻倍，如果从去年底部开始计算翻2倍。",
    "video_terms": "",
    "video_aspect": "9:16",
    "video_concat_mode": "random",
    "video_transition_mode": "None",
    "video_clip_duration": 3,
    "video_count": 1,
    "video_source": "local",
    "video_materials": [
        {
            "provider": "local",
            "url": "./storage/local_videos/1f36c2e9-8056-4e58-99ff-40852fceee4d_02陈永海.jpg",
            "duration": 0
        },
        {
            "provider": "local",
            "url": "./storage/local_videos/f7fcac65-06ce-4b6b-8697-4b142612e626_02顾宏地.jpg",
            "duration": 0
        },
        {
            "provider": "local",
            "url": "./storage/local_videos/e0472edc-8a6e-4234-bf32-d683d0ab9c2c_02何小鹏.jpg",
            "duration": 0
        },
        {
            "provider": "local",
            "url": "./storage/local_videos/f2ffd0ad-ec85-4de9-b635-2acaba65f8d2_水手.mp4",
            "duration": 0
        }
    ],
    "video_language": "",
    "voice_name": "zh-CN-YunyangNeural-Male",
    "voice_volume": 1.0,
    "voice_rate": 1.0,
    "bgm_type": "random",
    "bgm_file": "",
    "bgm_volume": 0.2,
    "subtitle_enabled": true,
    "subtitle_position": "bottom",
    "custom_position": 70.0,
    "font_name": "MicrosoftYaHeiBold.ttc",
    "text_fore_color": "#FFFFFF",
    "text_background_color": true,
    "font_size": 60,
    "stroke_color": "#000000",
    "stroke_width": 1.5,
    "n_threads": 2,
    "paragraph_number": 1
}
    Returns:

    """