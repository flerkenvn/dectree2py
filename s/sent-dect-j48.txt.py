#!/usr/bin/python3
def classify(suffix, punctuation, nextword, prefixLength, prefix, preword):
	if suffix == "empty":
		if punctuation == "dot":
			if nextword == "empty":
				return "yes"
			if nextword == "lower":
				return "no"
			if nextword == "upper":
				if prefixLength <= 2:
					if prefix == "empty":
						return "yes"
					if prefix == "lower":
						return "yes"
					if prefix == "upper":
						return "no"
					if prefix == "capword":
						return "no"
					if prefix == "numeric":
						return "no"
					if prefix == "misc":
						return "no"
				if prefixLength > 2:
					if prefix == "empty":
						return "yes"
					if prefix == "lower":
						return "yes"
					if prefix == "upper":
						return "yes"
					if prefix == "capword":
						if preword == "empty":
							return "yes"
						if preword == "lower":
							return "no"
						if preword == "upper":
							return "yes"
						if preword == "capword":
							return "yes"
						if preword == "numeric":
							return "yes"
						if preword == "misc":
							return "yes"
					if prefix == "numeric":
						return "no"
					if prefix == "misc":
						return "no"
			if nextword == "capword":
				if prefixLength <= 1:
					if prefix == "empty":
						return "yes"
					if prefix == "lower":
						return "yes"
					if prefix == "upper":
						if preword == "empty":
							return "no"
						if preword == "lower":
							return "yes"
						if preword == "upper":
							return "no"
						if preword == "capword":
							return "no"
						if preword == "numeric":
							return "no"
						if preword == "misc":
							return "no"
					if prefix == "capword":
						return "yes"
					if prefix == "numeric":
						return "no"
					if prefix == "misc":
						return "yes"
				if prefixLength > 1:
					return "yes"
			if nextword == "numeric":
				if prefixLength <= 2:
					return "no"
				if prefixLength > 2:
					return "yes"
			if nextword == "misc":
				return "yes"
		if punctuation == "quest":
			if nextword == "empty":
				return "yes"
			if nextword == "lower":
				return "no"
			if nextword == "upper":
				return "no"
			if nextword == "capword":
				return "yes"
			if nextword == "numeric":
				return "yes"
			if nextword == "misc":
				return "yes"
		if punctuation == "exclam":
			if nextword == "empty":
				return "yes"
			if nextword == "lower":
				return "no"
			if nextword == "upper":
				if prefix == "empty":
					return "no"
				if prefix == "lower":
					if prefixLength <= 3:
						return "no"
					if prefixLength > 3:
						return "yes"
				if prefix == "upper":
					return "no"
				if prefix == "capword":
					return "no"
				if prefix == "numeric":
					return "no"
				if prefix == "misc":
					return "no"
			if nextword == "capword":
				return "yes"
			if nextword == "numeric":
				return "yes"
			if nextword == "misc":
				return "no"
		if punctuation == "colon":
			if nextword == "empty":
				return "yes"
			if nextword == "lower":
				return "no"
			if nextword == "upper":
				return "no"
			if nextword == "capword":
				return "no"
			if nextword == "numeric":
				return "no"
			if nextword == "misc":
				return "no"
	if suffix == "lower":
		return "no"
	if suffix == "upper":
		return "no"
	if suffix == "capword":
		return "no"
	if suffix == "numeric":
		return "no"
	if suffix == "misc":
		return "yes"
