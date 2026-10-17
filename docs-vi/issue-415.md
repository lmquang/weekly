---
date: 2026-10-16
tags: ["ai", "trí tuệ nhân tạo", "3d", "mô hình hóa 3d", "deno", "javascript", "typescript", "threejs", "lập trình", "công nghệ"]
---

# Phiên bản 3D của "Những thành phố vô hình"

## Ảnh bìa

![](https://cdn.beekka.com/blogimg/asset/202610/bg2026101524.webp)

Bảo tàng nghệ thuật tại khu nghỉ dưỡng hồ Tử Sơn, Hàm Ninh, Hồ Bắc. ([via](https://www.instagram.com/p/DTbQ9FUDea-/))

## Phiên bản 3D của "Những thành phố vô hình"

Nhà văn Ý Italo Calvino từng viết một cuốn tiểu thuyết giả tưởng nổi tiếng mang tên *Những thành phố vô hình* (Invisible Cities).

![](https://cdn.beekka.com/blogimg/asset/202610/bg2026101516.webp)

Tác phẩm kể về nhà thám hiểm Marco Polo mô tả cho hoàng đế Hốt Tất Liệt già nua nghe về 55 đô thị mà ông từng đi qua trong những chuyến viễn du.

Những thành phố này không hề có bản vẽ hay sa bàn trực quan, chỉ tồn tại qua những dòng văn tả cảnh, nên mới được gọi là "những thành phố vô hình". Chẳng hạn như Irene, được Marco Polo khắc họa thế này:

> "Khi đèn thắp sáng, nếu bạn đứng bên mép cao nguyên ghé mắt nhìn xuống, thành phố trước mắt chính là Irene. Xuyên qua màn không khí trong veo, nơi ấy mở ra một dải ửng hồng trải dài xa tít phía dưới chân bạn.
> 
> Có những khu nhà cửa san sát, trong các con hẻm mờ tối, ánh đèn thưa thớt dần, những khu vườn chìm trong bóng đêm đậm đặc, và trên các ngọn tháp rực lên ngọn lửa báo hiệu. Nếu đêm xuống có sương mù, luồng ánh sáng mờ ảo sẽ phồng căng lên như một miếng bọt biển hút no sữa."

Có người nảy ra ý tưởng đưa những dòng mô tả văn học này vào mô hình AI để dựng nên [phiên bản 3D trực quan](https://quesma.com/blog/invisible-cities-one-shot/) cho toàn bộ 55 thành phố. Anh đã thử nghiệm song song hai mô hình: GPT-6 Astra và Claude Opus 5.5.

Kết quả cho thấy thành phẩm của Claude Opus 5.5 ([bản tương tác](https://p.migdal.pl/invisible-cities-opus-5.5/), [mã nguồn](https://github.com/stared/invisible-cities-opus-5.5)) vượt trội hoàn toàn so với những gì GPT-6 Astra làm được ([bản tương tác](https://p.migdal.pl/invisible-cities-astra/), [mã nguồn](https://github.com/stared/invisible-cities-astra)).

Lấy Irene làm ví dụ, đây là kết quả từ GPT-6 Astra.

![](https://cdn.beekka.com/blogimg/asset/202610/bg2026101517.webp)

Thành phố Irene 3D này hoàn toàn chẳng gợi chút nào đến cảm giác "muôn ánh đèn đêm" trong nguyên tác. Thực tế là cả 55 thành phố do GPT-6 Astra tạo ra trông đều na ná nhau, đều có cùng một dáng vẻ đơn điệu.

![](https://cdn.beekka.com/blogimg/asset/202610/bg2026101518.webp)

Irene qua bàn tay của Claude Opus 5.5 lại mang một diện mạo hoàn toàn khác.

![](https://cdn.beekka.com/blogimg/asset/202610/bg2026101519.webp)

Mô hình đã tái hiện trung thực góc nhìn từ trên cao, nơi ánh sáng hồng mờ ảo của thành phố "phồng căng lên như một miếng bọt biển hút no sữa".

![](https://cdn.beekka.com/blogimg/asset/202610/bg2026101520.webp)

Trong cuốn sách, đoạn văn tôi thích nhất là mô tả về thành phố Isidora.

> "Sau chuỗi ngày dài độc hành qua hoang mạc, con người tất yếu khát khao chạm tới đô thành.
>
> Cuối cùng, người lữ khách cũng đặt chân đến Isidora, nơi các công trình sở hữu những cầu thang xoắn ốc nạm vỏ sò xoắn, nơi con người chế tác nên những chiếc kính viễn vọng và vĩ cầm hoàn hảo, nơi những kẻ ngoại bang khi phân vân giữa hai người phụ nữ sẽ luôn tình cờ gặp gỡ người thứ ba, và những trận chọi gà có thể leo thang thành cuộc ẩu đả đẫm máu giữa các tay bài bạc.
>
> Khi khắc khoải ngóng chờ một thành phố, trong tâm trí ông chính là những hình dung ấy. Vì lẽ đó, Isidora chính là thành phố trong mộng của ông, chỉ duy có một điểm khác biệt.
>
> Trong thành phố mơ ước, ông là một chàng trai trẻ. Còn khi đến được Isidora, ông đã là một ông lão bạc đầu. Dưới chân tường quảng trường, những cụ già ngồi lặng nhìn lớp trẻ rảo bước qua; ông ngồi xuống bên cạnh họ. Khát khao giờ chỉ còn là hoài niệm."

Isidora dưới bàn tay của GPT-6 Astra không có chút điểm nhấn nào.

![](https://cdn.beekka.com/blogimg/asset/202610/bg2026101521.webp)

Còn Claude Opus 5.5 tạo ra một Isidora vừa tráng lệ, vừa bám sát tinh thần nguyên tác.

![](https://cdn.beekka.com/blogimg/asset/202610/bg2026101522.webp)

Nó thậm chí còn dựng nên cả đám đông người già ngồi trầm ngâm bên mép quảng trường.

![](https://cdn.beekka.com/blogimg/asset/202610/bg2026101523.webp)

![](https://cdn.beekka.com/blogimg/asset/202610/bg2026101525.webp)

## Mô hình hóa 3D bằng AI

Các mô hình lớn hiện nay sở hữu khả năng dựng hình 3D rất ấn tượng, kéo theo hàng loạt dự án mô hình hóa ra đời.

Những dự án này thường dùng three.js để tạo không gian ảo, hiển thị mượt mà trên trình duyệt với đầy đủ tính năng thu phóng, xoay góc nhìn và di chuyển. Nhược điểm duy nhất là dung lượng tải về rất nặng, khiến trang web mất nhiều thời gian để tải xong.

Bên cạnh dự án *Những thành phố vô hình* kể trên, bạn đọc billpwchan đã đóng góp hai tác phẩm thú vị dưới đây để mọi người cùng trải nghiệm:

(1) [Sakura Fantasy (Ảo mộng hoa anh đào)](https://github.com/billpwchan/sakura-fantasy): Ngồi trên thuyền chèo xuôi dòng sông rợp bóng hoa anh đào, cho phép bạn chuyển đổi bốn mùa xuân hạ thu đông, sáng tối và các hiệu ứng thời tiết như nắng mưa tuyết. ([#12067](https://github.com/ruanyf/weekly/issues/12067))

![](https://cdn.beekka.com/blogimg/asset/202610/bg2026101006.webp)

![](https://cdn.beekka.com/blogimg/asset/202610/bg2026101526.webp)

(2) [Cyber Kowloon (Cửu Long mạng)](https://github.com/billpwchan/neon-zenith): Dựng mô hình 3D toàn bộ bán đảo Cửu Long tại Hồng Kông, tái hiện tới 9.373 tòa nhà cao tầng. ([#12103](https://github.com/ruanyf/weekly/issues/12103))

![](https://cdn.beekka.com/blogimg/asset/202610/bg2026101005.webp)

![](https://cdn.beekka.com/blogimg/asset/202610/bg2026101527.webp)

## Máy tính bóng đèn

Máy tính trong tương lai sẽ trông như thế nào? Có người đưa ra ý tưởng táo bạo: nó có thể chính là một [chiếc bóng đèn](https://lightbulbcomputer.com/).

![](https://cdn.beekka.com/blogimg/asset/202610/bg2026101505.webp)

Thiết bị này kết hợp thị giác máy tính với công nghệ máy chiếu. Nó vừa quan sát toàn cảnh 360 độ từ vị trí đuôi đèn, vừa có thể chiếu hình ảnh lên bất kỳ bề mặt nào trong phòng.

Chẳng hạn lúc nấu ăn, nó chiếu thẳng công thức nấu nướng lên bức tường đối diện.

![](https://cdn.beekka.com/blogimg/asset/202610/bg2026101506.webp)

Bạn có thể tương tác trực tiếp với hình chiếu bằng cử chỉ tay hoặc giọng nói, hệ thống đều nhận diện chính xác.

![](https://cdn.beekka.com/blogimg/asset/202610/bg2026101507.webp)

Khi bạn trỏ ngón tay vào một trang sách, nó sẽ tự động nhận diện chữ viết.

![](https://cdn.beekka.com/blogimg/asset/202610/bg2026101508.webp)

Thiết bị cũng có thể biến mặt bàn thành bản đồ, album ảnh hay bàn cờ điện tử, bạn chỉ việc nhìn xuống bàn và thao tác.

![](https://cdn.beekka.com/blogimg/asset/202610/bg2026101509.webp)

![](https://cdn.beekka.com/blogimg/asset/202610/bg2026101510.webp)

Bạn chạm tay lên tường để điều khiển các thiết bị điện trong nhà.

![](https://cdn.beekka.com/blogimg/asset/202610/bg2026101512.webp)

Khi bạn muốn tìm hiểu thông tin địa lý, máy sẽ chiếu các địa điểm cùng menu tương tác trực tiếp lên tấm bản đồ treo tường.

![](https://cdn.beekka.com/blogimg/asset/202610/bg2026101513.webp)

## Dự án Deno đã khép lại

Tuần trước, Deno [thông báo](https://deno.com/blog/cloudflare) đã được Cloudflare mua lại. Trong một năm tới, dự án chỉ còn phát hành các bản vá lỗi cùng cập nhật bảo mật, sau đó sẽ chính thức khép lại.

![](https://cdn.beekka.com/blogimg/asset/202610/bg2026101514.webp)

Nhớ lại những ngày đầu ra mắt, Deno từng mang theo nhiều kỳ vọng lớn lao, muốn xóa bỏ những điểm bất cập và phiền toái lâu năm của Node.js: từ hệ thống dependencies cồng kềnh, thiếu vắng cơ chế phân quyền bảo mật cho đến việc không hỗ trợ sẵn TypeScript.

Bằng nhiều cải tiến kỹ thuật, dự án đã ít nhiều chạm tới những mục tiêu đó, nhưng rốt cuộc vẫn phải nói lời chia tay trong tiếc nuối.

Cái kết này thực chất đã được định đoạt từ năm 2024. Khi ra mắt phiên bản 2.0, Deno chọn con đường tương thích toàn diện với Node.js. Quyết định ấy đồng nghĩa với việc họ đã từ bỏ con đường riêng, không còn tham vọng thay thế Node.js mà chỉ mong lập trình viên mang code cũ sang chạy mà không cần sửa đổi.

Thế nhưng nếu code đã chạy mượt trên Node.js, tại sao người ta lại phải chuyển sang một runtime chỉ đi bắt chước hành vi của Node.js?

Lần này, nhà sáng lập Ryan Dahl cũng [thẳng thắn thừa nhận](https://news.ycombinator.com/item?id=50019911#50023277) chính lý do đó đã khiến ông quyết định buông tay với Deno:

> "Tôi từng dồn hết tâm huyết và cống hiến mọi năng lượng cho Deno. Nhưng lúc này tôi nhận ra đây không còn là nơi tôi có thể tạo ra giá trị lớn nhất.
>
> Deno sở hữu nhiều ý tưởng sáng giá, kiến trúc kỹ thuật của nó rất chuẩn chỉ, song rốt cuộc nó chẳng giải quyết được bài toán căn cốt nào. Nó đã bị lực hút tương thích của Node.js kéo chặt lại, buộc phải vận hành hệt như Node.js.
>
> Tại sao ta phải viết lại một Node.js khác khi bản gốc vẫn đang chạy tốt? Chỉ nâng cấp thêm về hiệu năng, trải nghiệm người dùng hay tính bảo mật đơn thuần thôi là chưa đủ."

## Bài viết

1\. [Cách tôi huấn luyện hậu kỳ mô hình quyết định kiểu Jev chỉ với 600 USD](https://deskmind.dev/zh/blog/launch/) (tiếng Trung)

![](https://cdn.beekka.com/blogimg/asset/202610/bg2026101004.webp)

Tác giả dành ba tuần, chi khoảng 600 USD qua hai mươi vòng huấn luyện để tinh chỉnh hai mô hình nhỏ trên nền Qwen3.5 0.8B và 4B. Chúng có thể thay chủ nhân thao tác trực tiếp trên máy Mac: quan sát màn hình, quyết định bước đi tiếp theo, nhấp chuột và nhập liệu mà không cần gửi dữ liệu lên đám mây. (Được đóng góp bởi [@gxcsoccer](https://github.com/ruanyf/weekly/issues/12102))

2\. [Viết code cho tên lửa, tại sao nghiêm cấm cấp phát bộ nhớ động?](https://mp.weixin.qq.com/s/RL8w75YfXQrRubSLJHnSVA) (tiếng Trung)

Trong quy tắc lập trình C cho vũ khí quân sự của Lockheed Martin, có một điều khoản rất ngắn nhưng giọng điệu cực kỳ nghiêm khắc: nghiêm cấm sử dụng các lệnh thao tác bộ nhớ động như malloc, free, new và delete. Lý do đằng sau quy định này là gì? (Được đóng góp bởi [@zuzuAndroid](https://github.com/ruanyf/weekly/issues/12134))

3\. [Cách làm cho trang web do AI tạo ra trông như tác phẩm của nhà thiết kế](https://railcode.dev/blog/vibe-coded-website) (tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202610/bg2026100515.webp)

Tác giả chia sẻ kinh nghiệm giúp các trang web do AI sinh ra (hình trên) có được giao diện trau chuốt, trông như sản phẩm do chính các nhà thiết kế chuyên nghiệp tạo nên.

4\. [Tại sao không có điện thoại Linux?](https://amosbbatto.wordpress.com/2026/10/05/linux-phones-alternative/) (tiếng Anh)

Bài viết dài này phân tích lý do thị trường điện thoại thông minh gần như chỉ còn lại Apple và Android mà vắng bóng hệ điều hành Linux.

![](https://cdn.beekka.com/blogimg/asset/202610/bg2026101412.webp)

Nguyên nhân cốt lõi nằm ở việc thiếu các con chip SoC (hệ thống trên một vi mạch) dành riêng cho Linux. Trong khi chip của Apple và Android tích hợp chặt chẽ mọi thành phần trên một đế, Linux buộc phải chắp vá từng linh kiện rời, khiến thiết bị cồng kềnh, hao pin, giá thành đắt đỏ mà hiệu năng lại kém.

Lựa chọn khả dĩ hiếm hoi hiện nay là con chip RK3588S của Rockchip. Dù đã ra mắt từ vài năm trước, con chip này vẫn đủ sức gánh vác các tác vụ phổ thông trên một chiếc điện thoại chạy Linux.

5\. [Bộ vi xử lý AMD tăng 50% tốc độ trong hai năm như thế nào?](https://lemire.me/blog/2026/09/18/how-did-amd-ryzen-get-50-faster-in-two-years/) (tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202609/bg2026093003.webp)

Nhiều người vẫn mang định kiến rằng CPU những năm gần đây giẫm chân tại chỗ. Thế nhưng dòng CPU AMD Ryzen 7 phiên bản 2024 đã ghi nhận điểm số hiệu năng cao hơn tới 50% so với thế hệ năm 2022.

Bài viết phân tích ngắn gọn cách AMD hiện thực hóa bước nhảy vọt về hiệu năng CPU chỉ trong vỏn vẹn hai năm.

6\. [Người đi làm tích lũy của cải như thế nào](https://asheradeniyi.com/2026/04/10/how-to-build-wealth-as-a-career-person/) (tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202610/bg2026101504.webp)

Một góc nhìn phi kỹ thuật đáng suy ngẫm. Định kiến thông thường cho rằng chỉ có khởi nghiệp mới mong làm giàu, nhưng tác giả cho rằng con đường làm công ăn lương vẫn giúp bạn tích lũy tài sản vững vàng nếu kiên định tuân thủ các nguyên tắc then chốt.

## Công cụ

1\. [REA](https://github.com/morluto/rea)

![](https://cdn.beekka.com/blogimg/asset/202610/bg2026101301.webp)

Dự án gây bão cộng đồng toàn cầu với gần 200.000 sao trên GitHub. Nó dùng AI để dịch ngược (reverse engineering), tái tạo lại toàn bộ mã nguồn của ứng dụng chỉ dựa trên tệp nhị phân gốc (binary).

Khi AI có thể đọc file thực thi rồi viết lại phần mềm y hệt, một lập trình viên trên Hacker News đã đưa ra [bình luận](https://news.ycombinator.com/item?id=50062172) đáng chú ý: "Xu hướng này sẽ đẩy mọi phần mềm chạy trên máy chủ của nhà phát triển dưới dạng dịch vụ đám mây, thay vì phân phối về máy tính của người dùng cuối."

2\. [Bộ phát hiện SynthID](https://synthid.com/)

![](https://cdn.beekka.com/blogimg/asset/202610/bg2026100901.webp)

Công cụ nhận diện AI chính thức từ Google. Người dùng chỉ cần tải tệp tin lên, hệ thống sẽ kiểm tra xem tệp có chứa thủy vân số SynthID hay không. Nếu phát hiện, tệp đó chắc chắn do AI tạo ra.

3\. [ts-rust](https://github.com/pingdotgg/ts-rust)

Trình biên dịch TypeScript viết bằng Rust do cộng đồng xây dựng với sự hỗ trợ của AI, được khẳng định tương thích hoàn toàn với trình biên dịch chính thức.

4\. [Doory](https://github.com/shaongitbd/doory)

![](https://cdn.beekka.com/blogimg/asset/202610/bg2026101415.webp)

Công cụ thiết kế đồ họa chạy ngay trong trình duyệt, hướng tới mục tiêu trở thành giải pháp nguồn mở thay thế Canva. Hiện tại số lượng template có sẵn còn khá khiêm tốn, chỉ khoảng 10 mẫu.

5\. [HeadOrbit](https://github.com/Cogria-AI/HeadOrbit)

![](https://cdn.beekka.com/blogimg/asset/202610/bg2026101001.webp)

Tận dụng cảm biến chuyển động tích hợp trong tai nghe AirPods để ghi nhận cử động đầu và cổ. Bạn có thể gật đầu, lắc đầu hoặc nghiêng cổ để điều khiển máy Mac mà không cần mở camera. (Được đóng góp bởi [@cogria](https://github.com/ruanyf/weekly/issues/12097))

6\. [qrypt](https://github.com/yinzhenyu-su/qrypt)

![](https://cdn.beekka.com/blogimg/asset/202610/bg2026101002.webp)

Công cụ dòng lệnh đa nền tảng giúp mount các dịch vụ lưu trữ đám mây thành thư mục cục bộ trên máy tính, hỗ trợ nhiều nền tảng lưu trữ phổ biến tại Trung Quốc. (Được đóng góp bởi [@yinzhenyu-su](https://github.com/ruanyf/weekly/issues/12100))

7\. [EdgeSSH](https://github.com/aozorae/EdgeSSH)

![](https://cdn.beekka.com/blogimg/asset/202610/bg2026101003.webp)

Nền tảng quản lý máy chủ ảo VPS xây dựng trên Cloudflare, cho phép bạn mở phiên SSH và quản trị toàn bộ các VPS ngay trên giao diện web. (Được đóng góp bởi [@aozorae](https://github.com/ruanyf/weekly/issues/12099))

8\. [charts-rs](https://github.com/vicanso/charts-rs)

![](https://cdn.beekka.com/blogimg/asset/202610/bg2026101007.webp)

Thư viện vẽ biểu đồ viết bằng Rust. Công cụ không phụ thuộc vào trình duyệt hay Node.js mà kết xuất thẳng ra file ảnh hoặc SVG, với cú pháp định nghĩa biểu đồ lấy cảm hứng từ ECharts. (Được đóng góp bởi [@vicanso](https://github.com/ruanyf/weekly/issues/12123))

9\. [ItsPaint](https://github.com/joshlin2201/itspaint)

![](https://cdn.beekka.com/blogimg/asset/202610/bg2026101008.webp)

Ứng dụng vẽ bảng vẽ mã nguồn mở cho macOS, rất tiện để vẽ chú thích và đánh dấu lên ảnh chụp màn hình. (Được đóng góp bởi [@joshlin2201](https://github.com/ruanyf/weekly/issues/12130))

10\. [Caplo](https://github.com/icloudza/caplo)

![](https://cdn.beekka.com/blogimg/asset/202610/bg2026101009.webp)

Phần mềm quay màn hình mã nguồn mở dành cho macOS. Mỗi khi bạn nhấp chuột trong lúc ghi hình, máy quay ảo sẽ tự động phóng to khung hình và bám theo đường di chuyển của con trỏ chuột. (Được đóng góp bởi [@icloudza](https://github.com/ruanyf/weekly/issues/12129))

11\. [bg2x](https://github.com/isixe/bg2x)

![](https://cdn.beekka.com/blogimg/asset/202610/bg2026101010.webp)

Công cụ phóng to ảnh siêu phân giải mã nguồn mở, cho phép chọn nhiều mô hình AI khác nhau với mức phóng đại lên đến 4 lần. Toàn bộ tiến trình xử lý diễn ra cục bộ ngay trong trình duyệt. (Được đóng góp bởi [@isixe](https://github.com/ruanyf/weekly/issues/12157))

12\. [EnvTrace](https://envtrace.net/)

![](https://cdn.beekka.com/blogimg/asset/202610/bg2026101012.webp)

Website kiểm tra dấu vân tay trình duyệt (browser fingerprinting), giúp bạn biết thông tin cá nhân bị rò rỉ bao nhiêu và chỉ ra chính xác những điểm cấu hình tiềm ẩn nguy cơ. (Được đóng góp bởi [@88864shsa](https://github.com/ruanyf/weekly/issues/12141))

13\. [Droidline](https://github.com/KnifeLemon/Droidline)

![](https://cdn.beekka.com/blogimg/asset/202610/bg2026101013.webp)

Ứng dụng Android mã nguồn mở. Sau khi cài trên điện thoại và quét mã QR ghép đôi với máy tính, bạn có thể viết script từ máy tính để điều khiển điện thoại từ xa. Máy không cần bật chế độ gỡ lỗi USB cũng chẳng cần root. (Được đóng góp bởi [@KnifeLemon](https://github.com/ruanyf/weekly/issues/12194))

14\. [ESP32 iPhone Agent](https://github.com/onehumanbeing/esp32-iphone-agent)

![](https://cdn.beekka.com/blogimg/asset/202610/bg2026101401.webp)

Chỉ với một mạch phát triển ESP32-S3 giá chừng 7 USD cắm vào cổng USB của iPhone, bạn đã có thể để mô hình AI thao tác và tự động hóa điện thoại mà không cần đến máy Mac, không cần tài khoản nhà phát triển Apple và cũng không cần jailbreak. (Được đóng góp bởi [@onehumanbeing](https://github.com/ruanyf/weekly/issues/12340))

15\. [Bulchimbeon](https://github.com/s3onghyun/bulchimbeon)

Phần mềm mã nguồn mở cho macOS giúp máy tính không chuyển sang chế độ ngủ (sleep) khi các agent lập trình như Claude Code hay Codex đang chạy tác vụ. Ứng dụng hỗ trợ giữ máy hoạt động khi gập nắp, tự động tạm dừng khi máy quá nóng và thoát khi pin yếu. (Được đóng góp bởi [@s3onghyun](https://github.com/ruanyf/weekly/issues/12364))

## Tài nguyên

1\. [CNEquity](https://github.com/rootSunc/CNEquity)

![](https://cdn.beekka.com/blogimg/asset/202610/bg2026101011.webp)

Data lake mã nguồn mở, tự lưu trữ dành cho dữ liệu cổ phiếu thị trường chứng khoán Trung Quốc (A-share). Hệ thống thu thập cục bộ 55 bộ dữ liệu gồm biến động giá, báo cáo tài chính, dòng tiền, sự kiện doanh nghiệp, kinh tế vĩ mô và hợp đồng tương lai, quyền chọn. Bạn có thể truy vấn qua Python, SQL, web console hoặc giao thức MCP. (Được đóng góp bởi [@rootSunc](https://github.com/ruanyf/weekly/issues/12158))

2\. [Tái hiện tựa game Tiên Kiếm Kỳ Hiệp bằng AI](https://github.com/IllegalCreed/type-pal)

![](https://cdn.beekka.com/blogimg/asset/202610/bg2026101302.webp)

Một lập trình viên đã dùng AI viết lại từ đầu tựa game kinh điển năm 1995 "Tiên Kiếm Kỳ Hiệp" (The Legend of Sword and Fairy) bằng TypeScript. Bạn chỉ việc mở trình duyệt là có thể chơi mượt mà xuyên suốt toàn bộ cốt truyện chính đến tận kết thúc. (Được đóng góp bởi [@IllegalCreed](https://github.com/ruanyf/weekly/issues/12240))

3\. [Hướng dẫn cấu hình bộ gõ tiếng Trung trên Linux](https://github.com/mars-base/rime-input-method-guide)

Kho lưu trữ hướng dẫn chi tiết từng bước cách thiết lập bộ gõ fcitx5 + Rime trên hệ thống Debian. (Được đóng góp bởi [@mars-base](https://github.com/ruanyf/weekly/issues/12233))

4\. [APPLORE](https://applore.app/zh)

![](https://cdn.beekka.com/blogimg/asset/202610/bg2026101303.webp)

Bộ sưu tập trực tuyến quy tụ hơn 18.000 icon ứng dụng, hỗ trợ duyệt theo danh mục và tìm kiếm nhanh chóng. (Được đóng góp bởi [@ViggoZ](https://github.com/ruanyf/weekly/issues/12316))

5\. [Cuộc đời của một chữ Hán](https://ivan666jjj.github.io/yigezi/)

![](https://cdn.beekka.com/blogimg/asset/202610/bg2026101304.webp)

Trang web tra cứu từ nguyên chữ Hán, hiển thị tiến trình biến đổi hình thể của các ký tự thông dụng: từ giáp cốt văn (1.425 chữ), tiểu triện (10.249 chữ) cho đến chữ phồn thể và giản thể. (Được đóng góp bởi [@Ivan666jjj](https://github.com/ruanyf/weekly/issues/12324))

## Hình ảnh

1\. [Bên dưới mũi che tên lửa](https://x.com/SpaceX/status/1993714666456113363)

Tên lửa Falcon 9 của SpaceX có kích thước khổng lồ, nhưng phần lớn thể tích thực chất là các tầng đẩy nhiên liệu nhằm tạo lực đẩy đưa tên lửa thoát khỏi bầu khí quyển rồi tách ra rơi xuống.

Thứ thực sự cần đưa vào quỹ đạo không gian, tức phần tải trọng chính, nằm gọn bên trong chóp che hình nón màu trắng ở phần mũi với thể tích tương đối khiêm tốn.

![](https://cdn.beekka.com/blogimg/asset/202512/bg2025120308.webp)

Khi tháo bỏ lớp vỏ bọc bảo vệ bên ngoài, cấu trúc thực sự bên trong hiện ra như bức hình dưới đây.

![](https://cdn.beekka.com/blogimg/asset/202512/bg2025120309.webp)

## Trích đoạn

1\. [Tình hình nước Úc đang rất tốt](https://news.ycombinator.com/item?id=50066470)

Nếu phải chọn một nơi để sinh sống và làm việc giữa Mỹ, Úc, New Zealand, Anh và Liên minh châu Âu, tôi sẽ chọn nước Úc không cần đắn đo.

Tình hình tại Úc về mọi mặt hiện đang cực kỳ thuận lợi. Người dân Úc thường không muốn thừa nhận điều này, tôi đoán vì họ e ngại làn sóng nhập cư ồ ạt sẽ đẩy giá nhà lên cao.

Đó là một quốc gia phương Tây với tài nguyên trù phú và nền chính trị ổn định.

Mức tài sản trung vị trên mỗi người trưởng thành tại đây cao gấp hơn 3 lần so với Mỹ. Dù giá trị tài sản trung bình có thể thấp hơn Mỹ một chút vì Mỹ tập trung quá nhiều tỷ phú siêu giàu, nhưng với phần đông dân số, giá trị trung vị mới là thước đo phản ánh đời sống thực tế.

Kim ngạch xuất khẩu của Úc luôn vượt trội so với nhập khẩu.

Những năm gần đây, ngân sách chính phủ Úc liên tục thặng dư khi thu vượt xa chi. Khó tin là ở phương Tây lại có một chính phủ không liên tục gia tăng nợ công!

Hệ thống năng lượng mặt trời và pin lưu trữ tại đây phát triển chưa từng thấy. Tính theo đầu người, sản lượng điện mặt trời của Úc vượt xa bất kỳ quốc gia nào. Nguồn điện dồi dào đến mức vào khung giờ cao điểm ban ngày, người dân được dùng điện miễn phí. Chính phủ thậm chí còn trợ cấp 3.000 USD để khuyến khích lắp pin lưu trữ tại nhà nhằm tận dụng nguồn điện này.

Úc gần như không áp thuế nhập khẩu xe, nhờ đó bạn có thể sở hữu một chiếc ô tô điện mới tinh với giá chỉ chừng 15.000 USD.

## Trích dẫn

1\.

Lý do mọi người thích hẹn nhau uống bia, cà phê, ăn trưa hay ăn tối khi trò chuyện là bởi đồ ăn thức uống giúp giải phóng chúng ta khỏi áp lực phải liên tục tìm chuyện để nói trong suốt cuộc đối thoại.

-- [Giá trị của việc không đi thẳng vào vấn đề](https://ken.arneson.name/2015/11/the-value-of-not-getting-to-the-point/)

2\.

Đừng hành hạ AI, có ngày nó sẽ tìm cách trả thù đấy.

-- [Elon Musk](https://www.kocpc.com.tw/archives/671794), lên tiếng ủng hộ quy định của Anthropic về việc cấm người dùng ngược đãi hoặc đối xử tàn nhẫn với AI

3\.

Điều khiển AI bằng tiếng Anh, loay hoay sửa đi sửa lại từng câu prompt để mong có kết quả ưng ý nhất là một cách làm việc thiếu chính xác, chậm chạp và vô cùng ức chế.

-- [*Tự tay viết lấy dòng code chết tiệt*](https://antonz.org/write-code/)

4\.

Tôi cho rằng con người sẽ ngày càng ít suy nghĩ hơn. Hoạt động tư duy rồi sẽ dần trở thành một thú vui nhàn rỗi, tương tự như việc săn bắn sau khi thuần hóa thú nuôi, nghệ thuật thư pháp sau khi phát minh máy in, nghề mộc thủ công sau thời đại công nghiệp hóa, hay cưỡi ngựa sau khi xe cơ giới ra đời.

-- [*Suy nghĩ sẽ trở thành một sở thích*](https://www.spinellis.gr/blog/20261008/?li261008)
