import json
import cv2


def preprocess(filepath, filename):
	data_in = shift_origin(filepath, filename)
	normalize(data_in)


def shift_origin(filepath, filename):
	total_frames=cv2.count_frames(filepath)
	total_body_points=18
	width = float(480)
	height = float(848)

	with open(filename, 'r') as json_file:
		data_in = json.load(json_file)
		data_out  = dict()
		for curr_frame_no in range(total_frames):
			curr_frame = data_in[str(curr_frame_no)]
			data_out[str(curr_frame_no)] = dict()
			for pnt_no in range(total_body_points):
				points = curr_frame[str(pnt_no)]['translate']
				new_x = width - float(points[0])
				new_y = height - float(points[1])
			
			data_out[str(curr_frame_no)][str(pnt_no)] = dict()
			data_out[str(curr_frame_no)][str(pnt_no)]['translate'] = [new_x, new_y]
		return json.dumps(data_out)


def min_max_normalize_util(v, old_l, old_h, new_l, new_h):
	new_v = (((v-old_l)/(old_h-old_l)) * (new_h-new_l)) + new_l
	return new_v


def normalize(data_in):
	data_out  = dict()
	for curr_frame_no in range(total_frames):
		curr_frame = data_in[str(curr_frame_no)]
		data_out[str(curr_frame_no)] = dict()
		for pnt_no in range(total_body_points):
			points = curr_frame[str(pnt_no)]['translate']
			new_x = min_max_normalize_util(float(points[0]), float(0), old_width, float(0), new_width)
			new_y = min_max_normalize_util(float(points[1]), float(0), old_height, float(0), new_height)
			
			data_out[str(curr_frame_no)][str(pnt_no)] = dict()
			data_out[str(curr_frame_no)][str(pnt_no)]['translate'] = [new_x, new_y]
	
	with open(f'shift_and_scale_{filename}.json', 'w+') as out_file:
		json.dump(data_out, out_file)
