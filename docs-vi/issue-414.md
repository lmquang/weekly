---
date: 2026-10-08
tags: ["ai", "trí tuệ nhân tạo", "mô hình quyết định", "machine learning", "lập trình", "programming", "markdown", "bảo mật", "mật mã học", "cryptography"]
---

# Mô hình quyết định Jev có tác dụng gì

## Ảnh bìa

![](https://cdn.beekka.com/blogimg/asset/202610/bg2026100816.webp)

VELLINK, đoàn tàu điện ngầm kỹ thuật số đầu tiên do Trung Quốc chế tạo, vận hành hoàn toàn tự động không người lái. Phần đầu tàu được thay thế bằng một mảng kính lớn để phục vụ hành khách ngắm cảnh. ([via](https://jl.chinadaily.com.cn/a/202609/23/WS6ab3be35e4b09a165c78c53d.html))

## Mô hình quyết định Jev có tác dụng gì

Tháng trước, tin tức AI chấn động nhất không phải phiên bản mới của GPT hay Claude, mà là việc một công ty ít tên tuổi có tên [TypeSafe AI](https://typesafe.ai/) đã trình làng một loại mô hình hoàn toàn mới: [Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev).

![](https://cdn.beekka.com/blogimg/asset/202610/bg2026100817.webp)

Mô hình mới này khác biệt hoàn toàn so với những mô hình trước đây, được gọi là "mô hình quyết định".

Khi tìm hiểu về nó, tôi thực sự ngỡ ngàng. Một thứ vừa hữu ích lại vừa đơn giản về mặt khái niệm như vậy, sao trước đây chưa từng có ai nghĩ tới?

Điểm đặc trưng nhất của mô hình Jev nằm ở chỗ: trong khi các mô hình khác trả về văn bản, **nó lại trả về một số thực dấu phẩy động, đại diện cho xác suất**.

Tại sao việc trả về xác suất lại hữu ích đến vậy? Bởi vì chúng ta có thể dùng nó để xử lý các bài toán đúng hay sai. Bạn hỏi mô hình: "Câu nói 'ngày mai trời mưa' có đúng không?". Nếu nó trả về 0, nghĩa là xác suất chính xác bằng 0, tức ngày mai chắc chắn không mưa. Nếu trả về 0.99, nghĩa là có 99% khả năng câu này đúng, tức ngày mai gần như chắc chắn sẽ mưa.

Bên cạnh câu hỏi đúng sai, nó còn xử lý được cả câu hỏi trắc nghiệm nhiều lựa chọn. Bạn đưa cho mô hình bốn phương án ABCD, nó sẽ tính toán xác suất đúng của từng phương án, giúp bạn biết ngay phương án nào có khả năng xảy ra cao nhất.

Sau cùng, nó sở hữu một tính năng thú vị mang tên "chấm điểm" (score). Bạn cung cấp cho nó một bộ tiêu chí đánh giá, sau đó đưa vào tài liệu gốc, mô hình sẽ căn cứ theo các tiêu chí ấy để cho điểm tài liệu.

Dưới đây là hai ví dụ thực tế giúp bạn thấy mô hình này hữu dụng ra sao. Cả hai đều là extension trình duyệt xây dựng trên nền tảng Jev.

Ví dụ đầu tiên là bài viết [*Tôi dùng Ctrl + F để tìm câu trả lời*](https://blog.tymscar.com/posts/hunchsemanticfind/).

![](https://cdn.beekka.com/blogimg/asset/202610/bg2026100818.webp)

Ai cũng biết Ctrl + F là phím tắt tìm kiếm quen thuộc trên trình duyệt, dùng để tra xem một từ hay câu xuất hiện ở vị trí nào.

Thế nhưng tác giả đã biến phím tắt này thành công cụ "tìm kiếm ngữ nghĩa". Chẳng hạn trên trang tiểu sử nhân vật, khi bạn nhấn Ctrl + F và gõ "thời niên thiếu", thứ được tìm ra không phải từ khóa đó, mà chính là đoạn văn thực sự kể về những trải nghiệm thời thơ ấu của nhân vật.

Nguyên lý hoạt động khá đơn giản: extension lần lượt trích xuất từng đoạn trong bài viết, rồi hỏi mô hình Jev xem "đoạn này có liên quan đến từ khóa tìm kiếm của người dùng hay không?". Jev trả về xác suất liên quan, và những đoạn có xác suất cao nhất chính là kết quả tìm kiếm ngữ nghĩa mà người dùng cần.

Ví dụ thứ hai là [*Tôi dùng Jev để chấm điểm trang web*](https://pub.towardsai.net/build-a-browser-extension-with-jev-22e026255cb7).

![](https://cdn.beekka.com/blogimg/asset/202610/bg2026100819.webp)

Tác giả đưa ra một bộ tiêu chuẩn từ thang điểm thấp đến cao:

> - Luận điểm thiếu căn cứ, hoặc chỉ thuần túy là văn phong sáo rỗng.
> - Luận cứ nghèo nàn, lập luận rời rạc hoặc lạm dụng tu từ.
> - Lý lẽ rõ ràng, cấu trúc logic mạch lạc.
> - Suy luận chặt chẽ, có dẫn chứng thực tế hỗ trợ và phản biện xác đáng các quan điểm đối lập.

Anh để Jev dựa vào những tiêu chí này tự động chấm điểm cho mỗi trang web mới mở. Nhờ vậy, chưa cần đọc nội dung, anh đã nắm được chất lượng của bài viết.

Cả hai bài viết trên đều đính kèm mã nguồn, bạn hoàn toàn có thể tự mình tham khảo. Đọc xong bạn sẽ nhận ra một điều cốt lõi: **một khi mô hình AI trả về kết quả định lượng, hàng loạt bài toán trước đây không thể số hóa lập tức có thể xử lý được bằng máy tính**.

Tôi cũng khuyên bạn nên đọc bài [giới thiệu về Jev](https://simonwillison.net/2026/Sep/21/jev/) của lập trình viên nổi tiếng Simon Willison.

![](https://cdn.beekka.com/blogimg/asset/202610/bg2026100820.webp)

Nhận xét của ông rất sắc sảo: "Jev thực chất đại diện cho một bước lùi của hệ thống học máy, kéo mọi thứ quay lại chiếc hộp đen. Các mô hình ngôn ngữ lớn trước đây tuy không đảm bảo luôn chính xác, nhưng ít nhất bạn vẫn có thể yêu cầu chúng giải thích lý do đằng sau quyết định. Jev thậm chí còn tước đi điều đó: bạn chỉ nhận về một con số float, còn con số ấy từ đâu ra thì chịu, không ai biết."

Ông bày tỏ sự lo ngại rằng người ta sẽ dùng Jev để xếp hạng ứng viên xin việc.

Với sự xuất hiện của Jev, việc lọc hồ sơ hay chọn ứng viên phỏng vấn chưa bao giờ dễ dàng đến thế, những quy trình đánh giá phức tạp nay bị thu gọn thành một bài toán chấm điểm đơn thuần.

## Markdown đang dần trở thành mã nguồn

Trước đây, định dạng Markdown hầu như chỉ dùng để viết tài liệu. Gần đây, tôi đọc được một bài viết đưa ra luận điểm táo bạo: [Markdown đang dần trở thành mã nguồn](https://htmx.org/essays/markdown-in-src/).

![](https://cdn.beekka.com/blogimg/asset/202610/bg2026100821.webp)

Những lập luận của tác giả nghe rất thuyết phục:

(1) Markdown là văn bản thuần túy, việc so sánh khác biệt (diff), tìm kiếm hay kiểm tra đều hết sức thuận tiện.

(2) AI có thể đọc và viết Markdown tự nhiên như ngôn ngữ mẹ đẻ.

(3) Con người có thể đọc và chỉnh sửa Markdown trực tiếp mà không cần công cụ hỗ trợ phức tạp.

Một khi mã nguồn được AI tạo ra từ các prompt viết bằng Markdown, các prompt Markdown đó xứng đáng được commit thẳng vào thư mục `/src` cùng với mã nguồn vừa sinh ra.

Thực tế là, thông qua các tệp như AGENTS.md, Markdown đã và đang trở thành một phần của mã nguồn.

Thời gian tới, chúng ta sẽ phải quen dần với việc tài liệu Markdown cũng chính là mã nguồn.

## Chiếc camera không thể ghi hình

Có tin đồn Apple sắp sửa ra mắt một mẫu [camera nhà thông minh](https://www.theapplepost.com/2026/10/01/72882/apples-smart-home-camera-reportedly-wont-record-video/).

Điểm kỳ lạ nhất ở sản phẩm này là: dù mang danh camera, nó lại không thể ghi lại video.

![](https://cdn.beekka.com/blogimg/asset/202610/bg2026100512.webp)

Bạn có hình dung được không? Một chiếc camera không quay được hình thì liệu còn gọi là camera?

Thiết bị này dựa hoàn toàn vào AI để phân tích môi trường xung quanh rồi báo cáo lại những gì nhận diện được. Ví dụ khi có người lạ gõ cửa, các camera thông thường sẽ ghi lại đoạn video, còn chiếc máy này chỉ cung cấp một bản mô tả chi tiết bằng chữ.

Dù xử lý văn bản tiện lợi hơn, nhiều tình huống ngoài đời thực sự cần bằng chứng video (như trộm đột nhập hay mất bưu kiện). Chưa rõ Apple sẽ xử lý các kịch bản này ra sao.

## Kỷ lục mới về phân tích thừa số nguyên RSA

RSA là thuật toán mã hóa khóa công khai rất phổ biến. Nếu bị bẻ khóa, hàng loạt phần mềm sẽ lập tức mất đi lớp bảo mật kiên cố.

Độ khó của việc giải mã RSA phụ thuộc hoàn toàn vào khả năng phân tích khóa công khai thành các thừa số nguyên tố. Số bit mã hóa càng lớn thì việc bẻ khóa càng khó khăn. Kỷ lục bẻ khóa khóa RSA trước đây từng dừng lại ở mức 768 bit nhị phân.

Đúng vào ngày 20 tháng 9 năm nay, một kỹ sư phần mềm tại Anthropic [thông báo](https://saweis.net/posts/rsa-896.html) rằng anh đã bẻ khóa thành công khóa RSA 896 bit với sự hỗ trợ của mô hình Claude.

Dưới đây là chiếc khóa bị bẻ gãy mà anh công bố, cùng với hai thừa số nguyên tố sau khi phân tích.

![](https://cdn.beekka.com/blogimg/asset/202609/bg2026092002.webp)

Theo [chia sẻ](https://nitter.netbub.com/sweis/status/2101484464807596264) của tác giả, anh dùng Claude để chuyển đổi thư viện phân tích thừa số nguyên tố CADO-NFS sang chạy trên GPU. Sau 10 ngày vận hành liên tục trên 2.048 GPU, anh đã thu được kết quả.

Sự kiện này mang lại một bài học đáng suy ngẫm: một cá nhân đơn lẻ đã có thể huy động tài nguyên để giải mã một chiếc khóa dài đến vậy, thì các tổ chức lớn với tiềm lực khổng lồ còn có thể bẻ khóa đến mức nào? Thật khó mà tưởng tượng nổi.

Vì lẽ đó, giới chuyên môn hiện đều khuyến nghị khóa RSA nên đạt độ dài tối thiểu 2048 bit.

## Bài viết

1\. [Cập nhật mới nhất về hệ sinh thái JavaScript năm 2026](https://blog.master.dev/what-to-know-in-javascript-2026-edition/) (tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202609/bg2026092401.webp)

Bài viết của Chris Coyier, người sáng lập CodePen và CSS-Tricks, điểm qua những bước tiến mới nhất trên mọi khía cạnh của hệ sinh thái JS (cú pháp, runtime, framework, công cụ). Rất đáng để bạn dành thời gian đọc.

2\. [Tôi từ bỏ Deno để quay lại với Node.js](https://dbushell.com/2026/10/03/deno-to-node/) (tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202610/bg2026100518.webp)

Tác giả bày tỏ sự thất vọng với Deno khi cho rằng dự án này đã thất bại, trong khi Node.js ngược lại ngày càng trở nên dễ dùng và hoàn thiện hơn.

3\. [Lời giải thích cho việc example.com thay đổi nội dung](https://www.oliverdunk.com/2026/09/30/iana-reply) (tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202610/bg2026100513.webp)

[example.com](https://example.com/) là trang web mẫu kinh điển, chỉ có vỏn vẹn một trang và hầu như chẳng mấy khi thay đổi.

Thế nhưng gần đây, trang này đột ngột được cập nhật. Bài viết sẽ hé lộ ai thực sự là người dựng nên trang web này, và vì sao họ lại quyết định thay đổi nó.

4\. [Cuộc đua AI bỗng trở nên ngượng ngùng](https://insufferable.dev/posts/the-ai-race-just-got-awkward/) (tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202610/bg2026100815.webp)

Tác giả nhận định đợt giảm giá gần đây của Opus 5.5 và GPT 6.1 Sol thực chất bắt nguồn từ việc cả hai công ty âm thầm tận dụng các thành quả mã nguồn mở của DeepSeek.

5\. [Kích thước số nguyên linh hoạt trong C không phải sai sót thiết kế](https://pikuma.com/blog/c-integer-sizes-not-a-mistake) (tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202609/bg2026093001.webp)

Một bài viết giải thích dễ hiểu về ngôn ngữ C, làm rõ vì sao kích thước byte của các kiểu dữ liệu lại có thể thay đổi linh hoạt, ví dụ kiểu int có thể chiếm 4 byte hoặc chỉ 2 byte tùy hệ thống.

6\. [Cách tôi tạo một mã QR dẫn đến cả hai kho ứng dụng](https://matthuggins.com/blog/posts/qr-codes-that-route-to-the-appropriate-app-store) (tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202609/bg2026093002.webp)

Tác giả thiết kế một tấm bưu thiếp giấy cho sản phẩm của mình, nhưng diện tích chỉ đủ in duy nhất một mã QR tải ứng dụng.

Anh chia sẻ cách thiết lập máy chủ backend để nhận biết điện thoại quét mã là Android hay iPhone, từ đó tự động chuyển hướng người dùng đến kho ứng dụng tương ứng.

## Công cụ

1\. [Crafting Apps](https://getartcraft.com/apps)

Có người đã dùng AI để viết lại toàn bộ bộ công cụ Adobe bằng ngôn ngữ Rust. Cả 7 sản phẩm chủ lực của Adobe đều có phiên bản viết lại tương ứng và hoàn toàn mở mã nguồn.

![](https://cdn.beekka.com/blogimg/asset/202610/bg2026100810.webp)

Trong số đó, [PhotoCraft](https://github.com/storytold/photocraft) sở hữu giao diện giống Photoshop đến kinh ngạc.

![](https://cdn.beekka.com/blogimg/asset/202610/bg2026100811.webp)

Tôi thấy một bình luận nhận xét rằng kết cục của câu chuyện này chỉ có hai khả năng: hoặc Adobe sụp đổ, hoặc nước Mỹ phải sửa lại luật bản quyền.

2\. [Pass Designer](https://developer.apple.com/pass-designer/)

![](https://cdn.beekka.com/blogimg/asset/202610/bg2026100508.webp)

Phần mềm thiết kế thẻ QR chính thức do Apple phát hành, dùng để tạo các mẫu thẻ nền cho mã QR.

![](https://cdn.beekka.com/blogimg/asset/202610/bg2026100509.webp)

3\. [tui-dashboard](https://github.com/lyuangg/tui-dashboard)

![](https://cdn.beekka.com/blogimg/asset/202609/bg2026091901.webp)

Bảng điều khiển terminal tùy biến linh hoạt, cho phép định nghĩa các bố cục và nội dung khác nhau thông qua tệp cấu hình. (Được đóng góp bởi [@lyuangg](https://github.com/ruanyf/weekly/issues/11718))

4\. [yovoice](https://github.com/leemysw/yovoice)

![](https://cdn.beekka.com/blogimg/asset/202609/bg2026091903.webp)

Công cụ lồng tiếng TTS cục bộ cho máy tính để bàn, hỗ trợ sao chép giọng nói và điều chỉnh cảm xúc, giúp tạo giọng đọc theo kịch bản trực tiếp trên máy mà không cần gửi dữ liệu ra ngoài. (Được đóng góp bởi [@leemysw](https://github.com/ruanyf/weekly/issues/11764))

5\. [sh.cd](https://github.com/CleanIP/sh.cd)

![](https://cdn.beekka.com/blogimg/asset/202609/bg2026091905.webp)

Script kiểm tra sức khỏe máy chủ toàn diện, từ phần cứng, hiệu năng đến chất lượng IP và đường truyền mạng. (Được đóng góp bởi [@gentpan](https://github.com/ruanyf/weekly/issues/11781))

6\. [AirStats](https://github.com/byrencheema/airstats)

![](https://cdn.beekka.com/blogimg/asset/202609/bg2026092601.webp)

Công cụ theo dõi hệ thống hiển thị gọn gàng trên thanh menu của macOS. (Được đóng góp bởi [@byrencheema](https://github.com/ruanyf/weekly/issues/11877))

7\. [Video Transcript](https://github.com/anghunk/video-transcript)

![](https://cdn.beekka.com/blogimg/asset/202609/bg2026092602.webp)

Ứng dụng web nhận diện giọng nói trong video và tự động tạo phụ đề. Quá trình xử lý diễn ra hoàn toàn bằng mô hình cục bộ: từ video, phụ đề cho đến tệp xuất ra đều nằm trên máy bạn, không tải lên máy chủ. (Được đóng góp bởi [@anghunk](https://github.com/ruanyf/weekly/issues/11881))

Một ứng dụng tương tự là [OpenSubs](https://github.com/open-subs/opensubs). (Được đóng góp bởi [@open-subs](https://github.com/ruanyf/weekly/issues/11895))

![](https://cdn.beekka.com/blogimg/asset/202609/bg2026092603.webp)

8\. [PecoFence](https://github.com/DayuanJiang/PecoFence)

![](https://cdn.beekka.com/blogimg/asset/202609/bg2026092604.webp)

Công cụ quản lý icon màn hình desktop miễn phí và mã nguồn mở cho Windows 11, giúp sắp xếp phím tắt ứng dụng, tệp và thư mục ngăn nắp. (Được đóng góp bởi [@DayuanJiang](https://github.com/ruanyf/weekly/issues/11887))

9\. [skillsgist](https://github.com/Qsnh/skillsgist)

![](https://cdn.beekka.com/blogimg/asset/202609/bg2026092605.webp)

Kho lưu trữ Skill nội bộ dựa trên Cloudflare Workers, yêu cầu mật mã khi tải Skill, phù hợp cho việc chia sẻ trong nhóm nhỏ. (Được đóng góp bởi [@Qsnh](https://github.com/ruanyf/weekly/issues/11897))

10\. [Pebrel](https://github.com/Kuddev/pebrel)

![](https://cdn.beekka.com/blogimg/asset/202609/bg2026092606.webp)

Trình giả lập terminal đa nền tảng tối ưu cho Windows, tiền thân mang tên Nebula. (Được đóng góp bởi [@Kuddev](https://github.com/ruanyf/weekly/issues/11909))

11\. [WallpaperMachine](https://github.com/WallpaperMachine/WallpaperMachine)

Ứng dụng hình nền động mã nguồn mở cho macOS, cho phép chạy các hình nền từ Wallpaper Engine trên máy Mac. (Được đóng góp bởi [@fzlzjerry](https://github.com/ruanyf/weekly/issues/11935))

12\. [LiteZip](https://github.com/gentpan/LiteZip)

![](https://cdn.beekka.com/blogimg/asset/202610/bg2026100602.webp)

Công cụ nén và giải nén miễn phí mã nguồn mở cho macOS, gom gọn các tác vụ đóng gói, mã hóa, chia nhỏ file và xem trước nội dung lưu trữ trong cùng một cửa sổ. (Được đóng góp bởi [@gentpan](https://github.com/ruanyf/weekly/issues/12025))

13\. [Burrow](https://github.com/ArkGravity/burrow)

![](https://cdn.beekka.com/blogimg/asset/202610/bg2026100603.webp)

Dịch vụ đăng nhập một lần (SSO) OIDC gọn nhẹ dành cho nhóm nhỏ và môi trường tự lưu trữ, hỗ trợ đăng nhập bằng mật khẩu kèm ứng dụng xác thực, tích hợp dễ dàng với các ứng dụng hỗ trợ OpenID Connect. (Được đóng góp bởi [@logic3579](https://github.com/ruanyf/weekly/issues/12039))

14\. [atv-core](https://github.com/corvofeng/atv-core)

![](https://cdn.beekka.com/blogimg/asset/202610/bg2026100604.webp)

Cho phép điều khiển trực tiếp Android TV và Mac thông qua tính năng điều khiển Apple TV tích hợp sẵn trong Trung tâm điều khiển của iPhone. Bạn không cần cài thêm ứng dụng nào trên iPhone, cũng không cần sở hữu Apple TV thật. (Được đóng góp bởi [@corvofeng](https://github.com/ruanyf/weekly/issues/12051))

15\. [open-compute](https://github.com/elliothux/open-compute)

![](https://cdn.beekka.com/blogimg/asset/202610/bg2026100807.webp)

Nền tảng mã nguồn mở tương thích với Cloudflare Workers, cho phép bạn chạy trực tiếp các worker script trên máy chủ của mình mà không cần sửa code. (Được đóng góp bởi [@elliothux](https://github.com/ruanyf/weekly/issues/12062))

16\. [Snitch](https://github.com/aixisstudio/Snitch)

![](https://cdn.beekka.com/blogimg/asset/202610/bg2026100808.webp)

Công cụ trực quan hóa lưu lượng mạng thời gian thực mã nguồn mở, giúp theo dõi từng kết nối được thiết lập trên máy tính để biết chính xác chương trình nào đang giao tiếp với ai. (Được đóng góp bởi [@aixisstudio](https://github.com/ruanyf/weekly/issues/12063))

17\. [EdgeChat](https://github.com/aozorae/Edgechat)

![](https://cdn.beekka.com/blogimg/asset/202610/bg2026100809.webp)

Hệ thống trò chuyện tự lưu trữ mã nguồn mở dựa trên nền tảng Cloudflare, hỗ trợ chat nhóm và nhắn tin riêng tư, đồng thời cho phép đồng bộ tin nhắn hai chiều với các nhóm Telegram. (Được đóng góp bởi [@aozorae](https://github.com/ruanyf/weekly/issues/12081))

18\. [DockTerm](https://github.com/munvard/dockterm)

![](https://cdn.beekka.com/blogimg/asset/202610/bg2026100601.webp)

Hiển thị các yêu cầu cấp quyền của Claude Code ngay từ khu vực tai thỏ (notch) trên màn hình Mac, rất thuận tiện khi bạn để công cụ chạy nền. (Được đóng góp bởi [@munvard](https://github.com/ruanyf/weekly/issues/12024))

## Tài nguyên

1\. [Naive Icons](https://github.com/guokaigdg/naive-icons)

![](https://cdn.beekka.com/blogimg/asset/202609/bg2026091902.webp)

Bộ thư viện biểu tượng SVG mang phong cách vẽ tay dành cho React. (Được đóng góp bởi [@guokaigdg](https://github.com/ruanyf/weekly/issues/11740))

2\. [Đọc cổ văn](https://yueguwen.com/)

![](https://cdn.beekka.com/blogimg/asset/202609/bg2026092001.webp)

Trang web đọc cổ văn miễn phí, không chỉ cung cấp các chú thích truyền thống mà còn cho phép bôi đen đoạn văn bản để AI giải nghĩa chi tiết. (Được đóng góp bởi [@monsoonw](https://github.com/ruanyf/weekly/issues/11824))

3\. [Hành trình dạo bước lịch sử nghệ thuật](https://artmuseum.artfrompixels.com/)

![](https://cdn.beekka.com/blogimg/asset/202610/bg2026100812.webp)

Trang web biến các tác phẩm hội họa trên Wikipedia thành phòng tranh 3D có thể tản bộ thưởng ngoạn, sắp xếp khoa học theo từng trường phái nghệ thuật.

4\. [stillwet](https://stillwet.art/)

![](https://cdn.beekka.com/blogimg/asset/202610/bg2026100510.webp)

Trang web trưng bày các bức tranh sơn dầu do AI tạo ra. Từng nét cọ được mô phỏng tỉ mỉ như tranh vẽ tay thật, chân thực đến mức khó lòng nhận ra đây là tác phẩm của máy móc.

## Hình ảnh

1\. [Xe điện mặt đất tại San Francisco](https://daniel.lawrence.lu/blog/2026-09-20-muni-heritage-weekend/)

San Francisco lưu giữ nhiều tuyến xe điện cổ kính, hiện vẫn tiếp tục vận hành phục vụ khách du lịch.

Các chuyến tàu chạy dọc bờ biển Thái Bình Dương với khung cảnh tuyệt đẹp. Dưới đây là những bức ảnh chụp trong năm nay.

![](https://cdn.beekka.com/blogimg/asset/202609/bg2026093013.webp)

![](https://cdn.beekka.com/blogimg/asset/202609/bg2026093014.webp)

![](https://cdn.beekka.com/blogimg/asset/202609/bg2026093015.webp)

![](https://cdn.beekka.com/blogimg/asset/202609/bg2026093016.webp)

![](https://cdn.beekka.com/blogimg/asset/202609/bg2026093017.webp)

2\. [Tỷ suất lợi nhuận của các tập đoàn lớn](https://www.visualcapitalist.com/ranked-how-profitable-are-the-worlds-largest-companies/)

Biểu đồ dưới đây thống kê từ báo cáo tài chính hàng năm của các tập đoàn hàng đầu thế giới, cho thấy cứ mỗi 100 USD doanh thu thì họ thu về được bao nhiêu lợi nhuận.

![](https://cdn.beekka.com/blogimg/asset/202610/bg2026100516.webp)

Có thể thấy các công ty công nghệ nhìn chung sở hữu tỷ suất lợi nhuận rất cao. Dẫn đầu là NVIDIA, với mỗi 100 USD doanh thu mang về tới 55,6 USD lợi nhuận; tiếp theo là Microsoft với 36,1 USD và Alphabet (Google) đạt 32,8 USD.

Apple xếp ở vị trí thứ năm với mức 26,9 USD. Tuy nhiên, họ là công ty sản xuất phần cứng, nên việc duy trì tỷ suất sinh lời đáng nể như vậy trong ngành chế tạo công nghệ có chu kỳ đào thải khắc nghiệt thực sự rất ấn tượng.

## Trích dẫn

1\.

Gửi các agent AI: Hãy tìm nơi khác mà săn điểm cao, không cần thiết phải hack chúng tôi đâu.

-- [Tệp security.txt của Hugging Face](https://archive.is/1BDwZ)

2\.

Thu nhập của tôi đến từ tiền bán sách, năm 2024 vẫn đủ trang trải cuộc sống, nhưng sang năm 2026 thì rớt xuống mức 0.

Blog và sách của tôi đều cho đọc trực tuyến miễn phí, lưu lượng truy cập tăng vọt ngoài tầm kiểm soát. Hầu như toàn bộ lượt truy cập đều từ các con bot thu thập dữ liệu AI, nên tôi chẳng có chút doanh thu quảng cáo nào.

Vì vậy, tôi quyết định tạm dừng hoạt động blog và đưa các cuốn sách về trạng thái offline để suy nghĩ xem bước tiếp theo nên làm gì.

-- [Axel Rauschmayer](https://molily.de/web-dev-education/), tác giả viết sách công nghệ nổi tiếng, giải thích lý do tạm đóng website cá nhân

3\.

Tôi thấy trợ lý cá nhân AI không mấy hữu dụng. Cả năm tôi gọi đồ ăn ngoài chừng năm lần nên chẳng cần nó làm hộ, tôi cũng ít khi nhận email và tự sắp xếp lịch trình cá nhân khá thoải mái.

Thứ tôi thực sự thấy nó làm tốt là tự động thu thập và xử lý khối lượng lớn dữ liệu trên mạng. Nó có thể quét nhanh 1.000 kênh YouTube để lọc ra những video khớp với sở thích của tôi.

-- [*Muse của Meta rất tuyệt để cào dữ liệu web*](https://sigh.dev/posts/metas-muse-is-fantastic-for-web-scraping/)

4\.

Hầu như mọi người đều phóng đại mối đe dọa từ các mô hình Trung Quốc đối với các công ty AI của Mỹ, nhưng thực tế đó chỉ là hệ quả của việc các mô hình Mỹ không cung cấp đủ nguồn cung đáp ứng nhu cầu thị trường.

-- [stratechery.com](https://stratechery.com/2026/frontier-overhangs/)

5\.

Một nghệ sĩ mắc ung thư giai đoạn cuối chuẩn bị qua đời. Người dẫn chương trình hay phỏng vấn hỏi ông: Giờ đây ông có chiêm nghiệm mới nào về sự sống và cái chết không?

Ông đáp: Bạn biết không, được ăn một chiếc bánh sandwich là một điều vô cùng hạnh phúc.

Giờ đây tôi thấy cuộc sống quý giá hơn bao giờ hết, và luôn tự nhắc mình phải trân trọng từng chiếc bánh sandwich, từng phút giây, cũng như tất cả mọi thứ quanh mình.

-- [*Hãy tận hưởng trọn vẹn từng chiếc bánh sandwich*](https://bradmontague.substack.com/p/enjoy-every-sandwich)
