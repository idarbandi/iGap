/**
 * این کامنت‌ها و داک‌استرینگ‌ها توسط من، Idarbandi، اضافه شده‌اند.
 * برای پشتیبانی بیشتر لطفاً با من تماس بگیرید: darbandidr99@gmail.com
 * GitHub: https://github.com/idarbandi/
 */

/**
 * رابطی که یک سرور را نشان می‌دهد.
 */
interface Server {
  id: number; // شناسه منحصر به فرد برای سرور
  name: string; // نام سرور
  description: string; // توضیحات سرور
  icon: string; // آدرس آیکون سرور
  category: string; // دسته‌بندی که سرور به آن تعلق دارد
  banner: string; // آدرس تصویر بنر سرور
}

/**
 * کامپوننت برای جستجو و بررسی سرورها بر اساس دسته‌بندی.
 *
 * از پارامترهای URL برای تعیین دسته‌بندی استفاده می‌کند و داده‌های سرور را بر اساس آن فراخوانی می‌کند.
 *
 * @returns {JSX.Element} کامپوننت ExploreServers.
 */
const ExploreServers = (): JSX.Element => {
  // استخراج نام دسته‌بندی از پارامترهای URL
  const { categoryName } = useParams();

  // ساخت URL بر اساس نام دسته‌بندی
  const url = categoryName ? `/server/?category=${categoryName}` : '/server/';

  // هوک سفارشی برای مدیریت عملیات CRUD و فراخوانی داده‌ها
  const { dataCRUD, fetchData } = useCrud<Server>([], url);

  // فراخوانی داده‌ها هر زمان که categoryName تغییر کند
  useEffect(() => {
    fetchData();
  }, [categoryName]);

  // اینجا JSX خود را برای نمایش داده‌های سرور اضافه کنید
  return (
    // مثال: نمایش نام‌های سرور
    <div>
      {dataCRUD.map((server) => (
        <div key={server.id}>{server.name}</div>
      ))}
    </div>
  );
};

export default ExploreServers;
