---
date: 2025-05-23
tags: ["ai", "trí tuệ nhân tạo", "neural network", "mạng nơ-ron", "deep learning", "học sâu", "imagenet", "gpu", "nvidia", "lập trình"]
---

# Những người khai sinh thuật toán mạng nơ-ron

## Ảnh bìa

![](https://cdn.beekka.com/blogimg/asset/202505/bg2025052105.webp)

Con đường xanh công cộng dọc hào thành cổ Bắc Kinh, gần Tháp Trống. ([via visuals_china@instagram](https://www.instagram.com/p/DJi3qkuOTZ5/))

## Những người khai sinh thuật toán mạng nơ-ron

Bài cảm nhận về [tự truyện của Fei-Fei Li](https://www.ruanyifeng.com/blog/2025/05/weekly-issue-348.html) tuần trước vẫn còn một đoạn tiếp theo.

Bài đó khép lại ở năm 2012, khi một đội Canada dùng thuật toán mạng nơ-ron để vô địch cuộc thi ImageNet.

Hôm nay, ta kể câu chuyện về đội ngũ ấy.

![](https://cdn.beekka.com/blogimg/asset/202505/bg2025052104.webp)

Qua đó, ta sẽ thấy thuật toán mạng nơ-ron ra đời thế nào, và ai đã âm thầm đẩy nó đi xa đến vậy.

**(1) Geoffrey Hinton** (1947-)

![](https://cdn.beekka.com/blogimg/asset/202505/bg2025051807.webp)

Hinton sinh ở Anh, sau đó chuyển đến Canada. Ông là người đặt nền móng và cũng là một trong những người phát minh chính của thuật toán mạng nơ-ron.

Khái niệm mạng nơ-ron xuất hiện vào cuối thập niên 1940, không phải do Hinton đề xuất. Lập luận khi ấy rất trực tiếp: con người suy nghĩ bằng mạng nơ-ron, vậy nếu máy mô phỏng được mạng nơ-ron, máy cũng có thể suy nghĩ.

Nhưng đó mới chỉ là ý tưởng, chưa có thuật toán cụ thể. Không ai biết phải khiến máy mô phỏng tư duy bằng cách nào.

Năm 1984, khi làm nghiên cứu sau tiến sĩ tại Đại học California, Hinton cùng hai đồng nghiệp đưa ra thuật toán lan truyền ngược.

Thuật toán này cho phép dựng mạng nhiều tầng và tạo ra đầu ra, biến mạng nơ-ron thành thứ có thể triển khai, đồng thời đặt nền tảng cho những thuật toán cao cấp hơn về sau.

Vì nó cần tính toán qua nhiều tầng, mỗi tầng sau học từ kết quả của tầng trước, cách làm này được gọi là "học sâu". Hinton từ đó được gọi là "cha đẻ của deep learning".

Nhờ đóng góp này, ông nhận giải Turing năm 2018 và giải Nobel Vật lý năm 2024.

**(2) Yann LeCun** (1960-)

![](https://cdn.beekka.com/blogimg/asset/202505/bg2025051808.webp)

Yann Andre Le Cun, tên tiếng Trung là Yang Likun, là người Pháp. Trong thập niên 1980, ông làm nghiên cứu sau tiến sĩ tại Đại học Toronto.

Cùng thời gian đó, Hinton đến giảng dạy ở Toronto và trở thành người hướng dẫn của ông.

Vì vậy, LeCun là học trò lớn của Hinton, người kế thừa rồi phát triển thuật toán ấy. Thành tựu chính của ông là đưa phép tích chập vào mạng nơ-ron, đồng thời tạo ra mạng nơ-ron đầu tiên có ứng dụng thực tế.

Trong thập niên 1990, ông dùng mạng nơ-ron để nhận dạng chữ số viết tay trên séc ngân hàng, và đã thuyết phục được doanh nghiệp sử dụng.

![](https://cdn.beekka.com/blogimg/asset/202505/bg2025051809.webp)

Nhưng ứng dụng này cũng phơi bày điểm yếu của mạng nơ-ron tích chập: nó cần lượng mẫu huấn luyện khổng lồ và sức mạnh tính toán rất lớn. Séc ngân hàng chỉ cần nhận ra mười chữ số Ả Rập, còn các bối cảnh đa dạng hơn thì phần cứng thời đó không kham nổi.

Giới học thuật vì thế kết luận rằng mạng nơ-ron tích chập chỉ hợp với những bài toán hẹp, ít tính toán và không đáng để mở rộng. Thuật toán này, cùng Hinton và LeCun, bị bỏ quên suốt hai thập kỷ.

Trong thời gian ấy, LeCun làm việc qua lại giữa phòng thí nghiệm doanh nghiệp và trường đại học. Khi thế giới nhìn nhận lại mạng nơ-ron tích chập, ông cùng Hinton nhận giải Turing năm 2018. Hiện ông là Phó chủ tịch kiêm nhà khoa học AI trưởng tại Meta.

**(3) Alex Krizhevsky** (1986-)

![](https://cdn.beekka.com/blogimg/asset/202505/bg2025051810.webp)

Alex Krizhevsky là người Ukraine, di cư sang Canada cùng gia đình khi còn nhỏ. Năm 2007, ông vào Đại học Toronto và trở thành nghiên cứu sinh tiến sĩ của Hinton.

Lúc đó, gần 20 năm đã trôi qua kể từ khi LeCun đề xuất mạng nơ-ron tích chập. Hinton chưa từng quên nó. Ông khuyến khích Alex và Ilya Sutskever, người sẽ được nhắc đến ngay sau đây, dùng thuật toán này để chinh phục ImageNet của Fei-Fei Li.

Alex viết một chương trình dùng 15 triệu ảnh của ImageNet để huấn luyện mạng nơ-ron tích chập. Khối lượng tính toán quá lớn khiến máy cá nhân không thể chạy nổi, nên ông mua hai card đồ họa Nvidia và để chúng tính toán liên tục 24 giờ mỗi ngày.

Thực tế cho thấy mạng nơ-ron tích chập, cộng bộ dữ liệu huấn luyện lớn và phần cứng tính toán nhanh, vượt qua mọi thuật toán đã biết khác. Cuối cùng, nhóm ba người của họ vô địch cuộc thi thuật toán ImageNet lần thứ ba năm 2012 với cách biệt rất lớn.

Sự kiện này gây chấn động ngành công nghệ. Các công ty Internet lớn đồng loạt mời Hinton và các học trò của ông. Baidu cũng đề nghị Hinton làm nhà khoa học trưởng, nhưng Google đã thắng cuộc cạnh tranh.

Năm 2013, Google mua công ty vỏ bọc do Hinton lập ra với giá 44 triệu USD, rồi tuyển cả Hinton, Alex và Ilya.

Alex nghỉ việc vào năm 2017. Hiện ông nghiên cứu công nghệ AI tại một startup.

**(4) Ilya Sutskever** (1986-)

![](https://cdn.beekka.com/blogimg/asset/202505/bg2025051811.webp)

Ilya Sutskever sinh ở Liên Xô cũ, sau đó đến Israel rồi Canada. Ông là bạn học tiến sĩ của Alex Krizhevsky tại Đại học Toronto, đồng thời cũng là nghiên cứu sinh của Hinton.

Ông lập nhóm cùng Alex và giành chiến thắng ở cuộc thi thuật toán ImageNet năm 2012. Hinton, với vai trò người hướng dẫn, cũng là một thành viên của nhóm.

Năm 2013, ông theo Hinton vào Google. Năm 2015, ông nghỉ việc để đồng sáng lập OpenAI và làm nhà khoa học trưởng, sau này trở thành một trong những tác giả chính của ChatGPT. Năm 2024, ông rời OpenAI và lập công ty AI riêng.

**(5) Andrej Karpathy** (1986-)

![](https://cdn.beekka.com/blogimg/asset/202505/bg2025051812.webp)

Andrej Karpathy sinh tại Slovakia, đến Canada cùng gia đình khi 15 tuổi và hoàn thành bậc cử nhân tại Đại học Toronto.

Ông có lẽ đã quen Ilya Sutskever từ thời đại học. Nhưng thay vì làm tiến sĩ ở Toronto, ông đến Đại học Stanford và học với Fei-Fei Li.

Hướng nghiên cứu của ông cũng là mạng nơ-ron tích chập. Trong thời gian làm tiến sĩ, ông mở và trực tiếp giảng dạy khóa deep learning đầu tiên của Stanford.

Năm 2015, ông gia nhập OpenAI cùng Ilya, trở thành một nhà nghiên cứu chủ chốt.

Năm 2017, ông rời OpenAI để đến Tesla làm Giám đốc AI, rồi nghỉ việc năm 2022.

**(6) Tổng kết**

Năm người trên là những người tạo dựng và thúc đẩy chủ yếu cho thuật toán mạng nơ-ron. Không có họ, sẽ không có các mô hình AI lớn ngày nay.

Nhưng chỉ thuật toán của họ thì AI vẫn không thể thành công. Thuật toán cần lượng dữ liệu khổng lồ để huấn luyện, còn huấn luyện cần phần cứng tính toán tốc độ cao. Không thể thiếu bất cứ mảnh nào trong ba mảnh ghép này.

Mãi đến năm 2012, mọi thứ mới đủ đầy: thuật toán mạng nơ-ron, bộ dữ liệu ImageNet của Fei-Fei Li và card đồ họa tốc độ cao của Nvidia cùng xuất hiện.

Lịch sử từ đó lật sang trang mới. Kỷ nguyên AI chính thức bắt đầu.

## Tin tức công nghệ

1. Một công ty ở Thâm Quyến ra mắt thứ có lẽ là [vỏ Raspberry Pi ngầu nhất](https://liliputing.com/pironman-5-max-turns-a-raspberry-pi-5-into-a-mini-tower-with-a-transparent-case-rgb-lighting-and-dual-nvme-ssd-support/).

![](https://cdn.beekka.com/blogimg/asset/202505/bg2025051009.webp)

Nó có màn hình trên vỏ, đèn RGB, quạt và bo mở rộng NVMe SSD, rất hợp để làm NAS hay chạy AI ở biên.

![](https://cdn.beekka.com/blogimg/asset/202505/bg2025051010.webp)

2. Phần Lan thử [sơn phản quang lên gạc tuần lộc](https://www.smithsonianmag.com/smart-news/avoid-deer-strikes-finland-painting-deer-antlers-reflective-paint-180949792/).

![](https://cdn.beekka.com/blogimg/asset/202504/bg2025042409.webp)

Mục tiêu là để tài xế dễ nhìn thấy tuần lộc vào ban đêm. Hiện mỗi năm có 4.000 con tuần lộc bị xe tông chết trên đường ở Phần Lan.

3. Phần mềm họp trực tuyến Google Meet ra mắt [dịch giọng nói trực tiếp](https://www.engadget.com/apps/google-brings-live-translation-to-meet-starting-with-spanish-174549788.html), trước hết dành cho tiếng Tây Ban Nha.

![](https://cdn.beekka.com/blogimg/asset/202505/bg2025052203.webp)

Trong cuộc họp, đối phương nói tiếng Tây Ban Nha nhưng bạn nghe tiếng Anh, còn giọng nói, ngữ điệu và cảm xúc vẫn giữ nguyên.

4. Arduino, công ty phần cứng mã nguồn mở của Ý, đang phát triển [PCB có thể phân hủy](https://blog.arduino.cc/2025/04/22/arduino-is-at-work-to-make-bio-based-pcbs/) để giảm ô nhiễm môi trường.

![](https://cdn.beekka.com/blogimg/asset/202505/bg2025051201.webp)

Loại bảng mạch này in đường mạch lên vật liệu lanh thực vật thay cho sợi thủy tinh và nhựa truyền thống.

Tuy vậy, đồng trên bảng mạch không thể phân hủy, nên cần thu hồi trước khi bỏ bảng mạch.

5. Một startup Mỹ chuẩn bị phóng vệ tinh để [đặt trung tâm dữ liệu AI ngoài không gian](https://www.ycombinator.com/companies/starcloud).

![](https://cdn.beekka.com/blogimg/asset/202505/bg2025051403.webp)

Nó dùng năng lượng Mặt Trời suốt 24 giờ và cũng không phải lo chuyện tản nhiệt.

Công ty hy vọng cách này giải được bài toán điện năng và làm mát của máy chủ AI.

## Bài viết

1. [Môi trường desktop Linux trên điện thoại](https://holdtherobot.com/blog/2025/05/11/linux-on-android-with-ar-glasses/) (Tiếng Anh)

Tác giả đi ra ngoài không mang laptop, chỉ cần điện thoại, bàn phím Bluetooth và kính AR.

![](https://cdn.beekka.com/blogimg/asset/202505/bg2025051903.webp)

Sau khi root điện thoại Android, ông cài một bản phân phối Linux bằng chroot, từ đó có thể chạy môi trường desktop.

![](https://cdn.beekka.com/blogimg/asset/202505/bg2025051904.webp)

2. [Logic cốt lõi của ứng dụng AI](https://sketch.dev/blog/agent-loop) (Tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202505/bg2025051905.webp)

Tác giả cho rằng logic cốt lõi của một ứng dụng AI, tức AI agent, chỉ cần chín dòng code.

3. [Các cổng bị trình duyệt chặn mặc định](https://www.keenformatics.com/ports-that-are-blocked-by-browsers) (Tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202505/bg2025051906.webp)

Có thể bạn chưa biết: trình duyệt không mở được `localhost:6000`, vì 6000 là cổng bị chặn mặc định.

4. [Khuyên dùng RustDesk cho desktop từ xa](https://www.xda-developers.com/i-tried-every-method-to-remotely-access-my-pc-this-method-is-the-best/) (Tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202504/bg2025040506.webp)

Khi dùng máy Mac để truy cập máy Windows, remote desktop là một cách làm. Tác giả khuyên dùng RustDesk.

5. [Mẹo CSS cho HTML `<dialog>`](https://cassidoo.co/post/css-for-dialogs/) (Tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202501/bg2025011910.webp)

HTML có phần tử popup gốc là `<dialog>`. Bài viết giới thiệu hai mẹo CSS đi kèm nó.

6. [Giải thích chi tiết cấu hình Git](https://blog.gitbutler.com/how-git-core-devs-configure-git/) (Tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202502/bg2025022504.webp)

Bài viết giải thích kỹ các thiết lập phổ biến nhất của lệnh `git config`.

## Công cụ

1. [Pyrefly](https://github.com/facebook/pyrefly/)

![](https://cdn.beekka.com/blogimg/asset/202505/bg2025051801.webp)

Trình kiểm tra kiểu cho code Python do Meta phát hành. Xem [bài giới thiệu](https://engineering.fb.com/2025/05/15/developer-tools/introducing-pyrefly-a-new-type-checker-and-ide-experience-for-python/).

2. [Zen Browser](https://github.com/zen-browser/desktop)

![](https://cdn.beekka.com/blogimg/asset/202505/bg2025052202.webp)

Trình duyệt mã nguồn mở mới, xây dựng trên Firefox, nhận được đánh giá rất tốt ở nước ngoài và có trải nghiệm sử dụng dễ chịu. Xem [bài giới thiệu](https://www.xda-developers.com/zen-browser-better-brave-arc-chrome/).

3. [xtool](https://github.com/xtool-org/xtool)

![](https://cdn.beekka.com/blogimg/asset/202505/bg2025051701.webp)

Một lựa chọn thay thế Xcode, dùng để phát triển ứng dụng iOS trên Linux, Windows và macOS.

4. [Zero Convert](https://nextbconvert.com/)

![](https://cdn.beekka.com/blogimg/asset/202505/bg2025051703.webp)

Công cụ chuyển đổi hàng loạt tệp trực tuyến, dùng WebAssembly và xử lý hoàn toàn trên máy cục bộ, đồng thời còn có thể chỉnh ảnh. ([@xiaoshangmin](https://github.com/ruanyf/weekly/issues/6864) đóng góp)

5. [Haozi Panel](https://github.com/tnb-labs/panel)

![](https://cdn.beekka.com/blogimg/asset/202505/bg2025051804.webp)

Panel quản lý máy chủ viết bằng Go. ([@devhaozi](https://github.com/ruanyf/weekly/issues/6881) đóng góp)

6. [Goravel](https://github.com/goravel/goravel)

![](https://cdn.beekka.com/blogimg/asset/202505/bg2025051805.webp)

Framework phát triển Web cho Go, giữ cách dùng tương đồng Laravel của PHP nên dễ bắt đầu nhanh. ([@devhaozi](https://github.com/ruanyf/weekly/issues/6882) đóng góp)

7. [OpenSpeedy](https://github.com/game1024/OpenSpeedy)

Công cụ mã nguồn mở thay đổi tốc độ game, thực hiện bằng cách điều chỉnh các hàm thời gian của Windows. ([@game1024](https://github.com/ruanyf/weekly/issues/6884) đóng góp)

8. [SimonAKing-Gallery](https://github.com/SimonAKing/AnimatedGallery)

![](https://cdn.beekka.com/blogimg/asset/202505/bg2025051901.webp)

Ứng dụng album ảnh JavaScript phía backend, hiển thị ảnh theo dạng thác nước. Chỉ cần chỉ định thư mục ảnh rồi chạy trực tiếp. ([@SimonAKing](https://github.com/ruanyf/weekly/issues/6886) đóng góp)

9. [Jwno](https://github.com/agent-kilo/jwno)

![](https://cdn.beekka.com/blogimg/asset/202505/bg2025052101.webp)

Trình quản lý cửa sổ lát gạch cho Windows 10/11 do cộng đồng mã nguồn mở phát triển, điều khiển bằng bàn phím. ([@agent-kilo](https://github.com/ruanyf/weekly/issues/6891) đóng góp)

10. [Mini program Xinghe](https://github.com/didi/dimina)

![](https://cdn.beekka.com/blogimg/asset/202505/bg2025052204.webp)

Framework đa nền tảng do Didi mã nguồn mở, hỗ trợ đóng gói mini program thành app native cho Android, iOS, HarmonyOS và Web. ([@dos1in](https://github.com/ruanyf/weekly/issues/6912) đóng góp)

## AI

1. [aTrain](https://github.com/JuergenFleiss/aTrain)

![](https://cdn.beekka.com/blogimg/asset/202505/bg2025051802.webp)

Công cụ nhận dạng giọng nói tự động đa nền tảng có giao diện đồ họa, dựa trên mô hình Whisper, nhận dạng được hơn 50 ngôn ngữ. Xem [bài giới thiệu](https://www.xda-developers.com/i-switched-from-otter-to-this-self-hosted-audio-transcription-app/).

2. [AI Image Editor](https://aiimageeditor.me/)

![](https://cdn.beekka.com/blogimg/asset/202505/bg2025051803.webp)

Công cụ xử lý ảnh trực tuyến miễn phí với hơn mười khả năng AI như cải thiện ảnh, xóa watermark và chuyển đổi phong cách. ([@worminone](https://github.com/ruanyf/weekly/issues/6883) đóng góp)

## Tài nguyên

1. [Museum of All Things](https://mayeclair.itch.io/museum-of-all-things)

Phần mềm desktop đa nền tảng biến Wikipedia thành một bảo tàng ảo.

![](https://cdn.beekka.com/blogimg/asset/202503/bg2025031008.webp)

Mỗi hiện vật tương ứng với một bài viết Wikipedia. Khung tranh trên tường là ảnh của bài viết, còn bảng thuyết minh là nội dung bài viết.

![](https://cdn.beekka.com/blogimg/asset/202503/bg2025031009.webp)

Các hành lang dẫn sang phòng trưng bày khác theo những liên kết trong bài viết, vì vậy gần như có vô hạn căn phòng để khám phá.

![](https://cdn.beekka.com/blogimg/asset/202503/bg2025031010.webp)

## Hình ảnh

1. [Robot trong Star Wars](https://www.facebook.com/groups/1740302472949408/permalink/3918177945161839)

Bộ phim Star Wars đầu tiên được quay năm 1976. Trong phim có robot R2-D2 có thể đi lại, làm nhiều động tác và nói chuyện.

![](https://cdn.beekka.com/blogimg/asset/202505/bg2025052106.webp)

Sự thật là nó chẳng hề công nghệ cao đến vậy. Khi quay phim, một diễn viên thật ngồi bên trong.

![](https://cdn.beekka.com/blogimg/asset/202505/bg2025052107.webp)

2. [Vì sao băng có thể tích lớn hơn?](https://nautil.us/five-things-we-still-dont-know-about-water-3383/)

Khi nước thành băng, thể tích tăng 10%, mật độ vì vậy thấp hơn nước và băng có thể nổi trên mặt nước.

Vì sao thể tích của băng lại tăng?

Câu trả lời nằm ở chỗ cấu trúc phân tử của băng khác cấu trúc phân tử của nước.

![](https://cdn.beekka.com/blogimg/asset/202203/bg2022031408.webp)

Phía trái hình trên là cấu trúc phân tử của nước lỏng, bên phải là của băng. Các nút màu trắng là nguyên tử hydro, nút đỏ là nguyên tử oxy.

Ta thấy nước lỏng tạo thành mạng liên kết sít sao, còn băng là mạng có nhiều khoảng rỗng. Cấu trúc phân tử của băng kém đặc khít hơn, nên thể tích lớn hơn.

## Trích đoạn

1. [URL của Slack](https://blog.jim-nielsen.com/2023/examples-of-great-urls/)

Slack là công ty phần mềm nhắn tin tức thời. Trang web của họ có trang "giới thiệu công ty", thông thường URL của trang này sẽ là `slack.com/about`, nhưng Slack không chọn cách đó.

Họ đặt tên trang là `is` và tách nó thành nhiều trang con.

Vì thế, URL cho trang "giới thiệu công ty" là `slack.com/is`.

URL của các trang con như sau.

> - slack.com/is/team-communication
> - slack.com/is/everything-in-one-place
> - slack.com/is/wherever-you-are

Lợi ích là chỉ nhìn URL đã biết trang muốn truyền đạt điều gì. Bản thân URL đã là một cách quảng bá công ty.

Cách dùng `is` khéo léo này về sau được nhiều nơi học theo. Tình cờ, `is` cũng là tên miền cấp cao nhất đại diện cho Iceland. Nhiều người nổi tiếng đăng ký tên miền `.is` làm trang cá nhân.

Chẳng hạn, website của nghệ sĩ Jessica Hische dùng tên miền `jessicahische.is`, và các URL giới thiệu của cô đều có dạng `jessicahische.is/xxx`.

## Trích dẫn

1\.

Chúng tôi sẽ sớm chia sẻ với mọi người một thành quả nghiên cứu kín đáo. Chúng tôi sẽ đặt cho nó một cái tên hay hơn chatGPT, phòng khi nó trở nên phổ biến.

-- [Sam Altman](https://x.com/sama/status/1923104596622246252), CEO của OpenAI

2\.

Định luật Gall thường được trích dẫn: "Một hệ thống phức tạp đang vận hành hiệu quả luôn tiến hóa từ một hệ thống đơn giản đang vận hành hiệu quả."

Nhưng hệ quả của nó ít khi được nhắc đến: "Một hệ thống phức tạp được thiết kế từ con số không sẽ không bao giờ hoạt động hiệu quả. Bạn phải bắt đầu bằng một hệ thống đơn giản có thể chạy."

-- [Stack Staves](https://www.stackstaves.net/post/2023-12-07-theres-more-to-that/)

3\.

Vũ trụ có hai khả năng: hoặc chúng ta cô độc, hoặc chúng ta không cô độc. Cả hai khả năng đều đáng sợ như nhau.

-- [Arthur C. Clarke](https://www.planetary.org/articles/the-fermi-paradox-where-are-all-the-aliens), nhà văn khoa học viễn tưởng nổi tiếng người Anh

4\.

Mặt Trời mất 230 triệu năm để quay một vòng quanh Ngân Hà. Lần trước nó ở vị trí này, khủng long vẫn thống trị Trái Đất.

-- [Người dùng Reddit](https://www.reddit.com/r/Paleontology/comments/18wqvba/it_takes_the_sun_230_million_years_to_orbit_once/)

5\.

Tôi theo dõi một số nhà giáo dục và tất cả họ đều kể cùng một hiện tượng: sinh viên dùng ChatGPT cho mọi việc, nên rốt cuộc chẳng học được gì.

Cuối cùng, có thể xuất hiện một thế hệ có năng lực tự thân rất thấp, phụ thuộc hoàn toàn vào những công nghệ họ không hiểu. Một khi công nghệ sụp đổ, họ sẽ không bao giờ tự xây lại mọi thứ từ đầu được.

-- [Neal Stephenson](https://simonwillison.net/2025/May/18/neal-stephenson/#atom-everything), nhà văn khoa học viễn tưởng Mỹ, người tạo ra thuật ngữ "Metaverse"
