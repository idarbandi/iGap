/**
 * این کامنت‌ها و داک‌استرینگ‌ها توسط من، Idarbandi، اضافه شده‌اند.
 * برای پشتیبانی بیشتر لطفاً با من تماس بگیرید: darbandidr99@gmail.com
 * GitHub: https://github.com/idarbandi/
 */

import useAxiosWithInterceptor from '../helpers/jwtinterceptor.ts';
import { BASE_URL } from '../config.ts';
import { useEffect, useState } from 'react';

/**
 * اینترفیس برای استفاده از CRUD.
 *
 * @template T نوع داده‌هایی که مدیریت خواهند شد.
 */
interface IuseCrud<T> {
  dataCRUD: T[]; // داده‌های CRUD
  fetchData: () => Promise<void>; // تابع برای فراخوانی داده‌ها
  error: Error | null; // خطا در صورت بروز
  isLoading: boolean; // وضعیت بارگذاری
}

/**
 * هوک سفارشی برای مدیریت عملیات CRUD.
 *
 * @template T نوع داده‌هایی که مدیریت خواهند شد.
 * @param {T[]} initalData داده‌های اولیه برای CRUD
 * @param {string} apiURL آدرس API برای فراخوانی داده‌ها
 * @returns {IuseCrud<T>} اینترفیس استفاده از CRUD
 */
const useCrud = <T>(initalData: T[], apiURL: string): IuseCrud<T> => {
  const jwtAxios = useAxiosWithInterceptor();
  const [dataCRUD, setDataCRUD] = useState<T[]>(initalData);
  const [error, setError] = useState<Error | null>(null);
  const [isLoading, setIsLoading] = useState(false);

  /**
   * تابع برای فراخوانی داده‌ها از API.
   */
  const fetchData = async () => {
    setIsLoading(true);
    try {
      const response = await jwtAxios.get(`${BASE_URL}${apiURL}`, {});
      const data = response.data;
      setDataCRUD(data);
      setError(null);
      setIsLoading(false);
      return data;
    } catch (error: any) {
      if (error.response && error.response.status === 400) {
        setError(new Error('400'));
      }
      setIsLoading(false);
      throw error;
    }
  };

  return { fetchData, dataCRUD, error, isLoading };
};

export default useCrud;
