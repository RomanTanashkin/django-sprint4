from django.core.paginator import Paginator
from django.db.models import Count
from django.utils import timezone

from .models import Post

POSTS_PER_PAGE = 10


def annotate_comment_count(queryset):
    return queryset.annotate(
        comment_count=Count('comments')
    ).order_by('-pub_date')


def published_posts_queryset():
    return annotate_comment_count(
        Post.objects
        .select_related('category', 'location', 'author')
        .filter(
            is_published=True,
            pub_date__lte=timezone.now(),
            category__is_published=True,
        )
    )


def paginate(request, queryset, per_page=POSTS_PER_PAGE):
    paginator = Paginator(queryset, per_page)
    page_number = request.GET.get('page')
    return paginator.get_page(page_number)
