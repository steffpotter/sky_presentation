FROM python:3.8-alpine as build

# copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt

# switch working directory
WORKDIR /app

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

# copy every content from the local file to the image
COPY . /app



# stage 2
FROM nginx:1.23.alpine
COPY --from=build /app/build /usr/share/nginx/html

COPY nginx/nginx.conf /etc/nginx/conf./default.conf

EXPOSE 80

CMD [ "nginx", "-g" , "daemon off;"]
