all:
	protoc --python_out=cfg_examples/ CFG.proto
	protoc --python_out=tools/ CFG.proto
