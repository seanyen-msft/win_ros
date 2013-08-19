/**
 * @file /include/%(package)s/%(package)s.hpp
 *
 * @brief Template class for %(package)s.
 **/
#ifndef %(package)s_HPP
#define %(package)s_HPP

#ifdef WIN32
  #ifdef %(package)s_EXPORTS
    #define %(package)s_API __declspec(dllexport)
  #else
    #define %(package)s_API __declspec(dllimport)
  #endif
#else
  #define %(package)s_API
#endif

namespace %(package)s
{
  /**
   * @brief Template class for $(package)s
   */
  class %(package)s_API Foo
  {

  public:
    Foo() {};

    void helloDude();
  };

} // namespace %(package)s

#endif // %(package)s_HPP
