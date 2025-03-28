select count(*) as FISH_COUNT
from fish_info
join fish_name_info
on fish_info.fish_type = fish_name_info.fish_type
where fish_name_info.fish_name in ('BASS', 'SNAPPER')
