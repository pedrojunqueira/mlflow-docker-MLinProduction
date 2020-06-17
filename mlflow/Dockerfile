FROM continuumio/miniconda:4.5.4

RUN pip install mlflow>=1.0 \
    && pip install numpy==1.14.3 \
    && pip install scipy \
    && pip install pandas==0.22.0 \
    && pip install scikit-learn \
    && pip install cloudpickle

WORKDIR /mnt/mlflow

RUN mkdir /model

COPY ./model /model

COPY run.sh /mnt/mlflow

RUN chmod +x /mnt/mlflow/run.sh 

CMD ["bash", "/mnt/mlflow/run.sh"]