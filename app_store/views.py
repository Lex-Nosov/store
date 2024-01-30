from django.views.generic import DetailView, ListView, UpdateView

from app_store.models import Product, Category


class GetCategories:

    def get_all_categories(self):
        return Category.objects.all()


class MainView(GetCategories, ListView):
    model = Product
    template_name = 'product_temp/product/main.html'


class ProductDetail(DetailView):
    model = Product
    template_name = 'product_temp/product/detail_product.html'


class ProductView(ListView):
    model = Product
    template_name = 'product_temp/product/products.html'
    context_object_name = 'products'

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.GET.get("category"):
            queryset = Product.objects.filter(category_field__name_category=self.request.GET.get("category"))
        if self.request.GET.get("q"):
            queryset = Product.objects.filter(name__iregex=self.request.GET.get("q"))
        return queryset

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['q'] = self.request.GET.get('q')
        return context
