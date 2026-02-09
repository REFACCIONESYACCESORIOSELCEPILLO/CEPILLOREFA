/** @odoo-module */

import { registry } from "@web/core/registry";
import { loadJS } from "@web/core/assets";
import { useService } from "@web/core/utils/hooks";

import { Component, onWillStart, useRef, onMounted, useState } from "@odoo/owl";

//  Top 5 Customer all charts


// Bar chart

export class VehicleChartRendorBar extends Component {
    setup() {
        this.chartRef = useRef("chart");
        this.orm = useService("orm");
        this.actionService = useService("action")
        this.state = useState({ timeFilter: "daily" });
        // this.actionService = useService("action")
        onWillStart(async () => {
            await loadJS("https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.3.0/chart.umd.min.js");
        });

        onMounted(async () => await this.renderChart());
    }

    async renderChart() {
        const saleOrderss = await this.orm.searchRead("sale.order", []);
        const partnerOrderCounts = saleOrderss.reduce((count, order) => {
            count[order.partner_id[0]] = (count[order.partner_id[0]] || 0) + 1;
            console.log(`Order ID: ${order.id} - Partner ID: ${order.partner_id[0]} - Partner Name: ${order.partner_id[1]}`);
            return count;
        }, {});

        const topPartners = Object.entries(partnerOrderCounts)
            .sort((a, b) => b[1] - a[1])
            .slice(0, 5)
            .map(async ([partnerId]) => {
                const partner = await this.orm.searchRead("res.partner", [['id', '=', partnerId]], ['name']);
                return { id: partnerId, name: partner[0]?.name || 'Unknown', orders: partnerOrderCounts[partnerId] };
            });

        const datas = await Promise.all(topPartners);

        datas.forEach((partner, index) => {
            console.log(`${index + 1}. ${partner.name} - Orders: ${partner.orders}`);
        });

        const labels = datas.map(partner => partner.name);
        const data = datas.map(partner => partner.orders);


        // const action = this.orm.call("sale.order", "viewSaleOrders",  {});
        // this.actionService.doAction(action);
        const backgroundColors = ["#FFB6C1", "#D8BFD8", "#87CEFA", "#FFFFE0", "#ADD8E6"];

        new Chart(this.chartRef.el, {
            type: "bar",
            data: {
                labels,
                datasets: [{
                    label: "Top 5 Customers",
                    data,
                    backgroundColor: backgroundColors,
                    hoverBackgroundColor: backgroundColors
                }],
            },
            options: { responsive: true },
        });
    }
}



export class VehicleChartRendordoughnut extends Component {
    setup() {
        this.chartRef = useRef("chart");
        this.orm = useService("orm");
        this.state = useState({ timeFilter: "daily" });

        onWillStart(async () => {
            await loadJS("https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.3.0/chart.umd.min.js");
        });

        onMounted(async () => await this.renderChart());
    }

    async renderChart() {
        const saleOrderss = await this.orm.searchRead("sale.order", []);
        const partnerOrderCounts = saleOrderss.reduce((count, order) => {
            count[order.partner_id[0]] = (count[order.partner_id[0]] || 0) + 1;
            console.log(`Order ID: ${order.id} - Partner ID: ${order.partner_id[0]} - Partner Name: ${order.partner_id[1]}`);
            return count;
        }, {});

        const topPartners = Object.entries(partnerOrderCounts)
            .sort((a, b) => b[1] - a[1])
            .slice(0, 5)
            .map(async ([partnerId]) => {
                const partner = await this.orm.searchRead("res.partner", [['id', '=', partnerId]], ['name']);
                return { id: partnerId, name: partner[0]?.name || 'Unknown', orders: partnerOrderCounts[partnerId] };
            });

        const datas = await Promise.all(topPartners);

        datas.forEach((partner, index) => {
            console.log(`${index + 1}. ${partner.name} - Orders: ${partner.orders}`);
        });

        const labels = datas.map(partner => partner.name);
        const data = datas.map(partner => partner.orders);


        // const backgroundColors = ["#CDA0E6", "#FF91A4", "#A0E6E6", "#FF99CC", "#FFD580"];
        const backgroundColors = ["#FFB6C1", "#D8BFD8", "#87CEFA", "#FFFFE0", "#ADD8E6"];

        new Chart(this.chartRef.el, {
            type: "doughnut",
            data: {
                labels,
                datasets: [{
                    label: "Top 5 Customers",
                    data,
                    backgroundColor: backgroundColors,
                }],
            },
            options: { responsive: true },
        });
    }
}

// pie chart 
export class VehicleChartRendorpie extends Component {
    setup() {
        this.chartRef = useRef("chart");
        this.orm = useService("orm");
        this.state = useState({ timeFilter: "daily" });
        this.actionService = useService("action")

        onWillStart(async () => {
            await loadJS("https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.3.0/chart.umd.min.js");
        });

        onMounted(async () => await this.renderChart());
    }

    async renderChart() {
        const saleOrderss = await this.orm.searchRead("sale.order", []);
        const partnerOrderCounts = saleOrderss.reduce((count, order) => {
            count[order.partner_id[0]] = (count[order.partner_id[0]] || 0) + 1;
            console.log(`Order ID: ${order.id} - Partner ID: ${order.partner_id[0]} - Partner Name: ${order.partner_id[1]}`);
            return count;
        }, {});

        const topPartners = Object.entries(partnerOrderCounts)
            .sort((a, b) => b[1] - a[1])
            .slice(0, 5)
            .map(async ([partnerId]) => {
                const partner = await this.orm.searchRead("res.partner", [['id', '=', partnerId]], ['name']);
                return { id: partnerId, name: partner[0]?.name || 'Unknown', orders: partnerOrderCounts[partnerId] };
            });

        const datas = await Promise.all(topPartners);

        datas.forEach((partner, index) => {
            console.log(`${index + 1}. ${partner.name} - Orders: ${partner.orders}`);
        });

        const labels = datas.map(partner => partner.name);
        const data = datas.map(partner => partner.orders);


        // const backgroundColors = ["#CDA0E6", "#FF91A4", "#A0E6E6", "#FF99CC", "#FFD580"];
        const backgroundColors = ["#FFB6C1", "#D8BFD8", "#87CEFA", "#FFFFE0", "#ADD8E6"];


        new Chart(this.chartRef.el, {
            type: "pie",
            data: {
                labels,
                datasets: [{
                    label: "Top 5 Customers",
                    data,
                    backgroundColor: backgroundColors,
                }],
            },
            options: { responsive: true },
        });
    }
}


// line chart
export class VehicleChartRendorline extends Component {
    setup() {
        this.chartRef = useRef("chart");
        this.orm = useService("orm");
        this.state = useState({ timeFilter: "daily" });

        onWillStart(async () => {
            await loadJS("https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.3.0/chart.umd.min.js");
        });

        onMounted(async () => await this.renderChart());
    }

    async renderChart() {
        const saleOrderss = await this.orm.searchRead("sale.order", []);
        const partnerOrderCounts = saleOrderss.reduce((count, order) => {
            count[order.partner_id[0]] = (count[order.partner_id[0]] || 0) + 1;
            console.log(`Order ID: ${order.id} - Partner ID: ${order.partner_id[0]} - Partner Name: ${order.partner_id[1]}`);
            return count;
        }, {});

        const topPartners = Object.entries(partnerOrderCounts)
            .sort((a, b) => b[1] - a[1])
            .slice(0, 5)
            .map(async ([partnerId]) => {
                const partner = await this.orm.searchRead("res.partner", [['id', '=', partnerId]], ['name']);
                return { id: partnerId, name: partner[0]?.name || 'Unknown', orders: partnerOrderCounts[partnerId] };
            });

        const datas = await Promise.all(topPartners);

        datas.forEach((partner, index) => {
            console.log(`${index + 1}. ${partner.name} - Orders: ${partner.orders}`);
        });

        const labels = datas.map(partner => partner.name);
        const data = datas.map(partner => partner.orders);


        const backgroundColors = ["#CDA0E6", "#FF91A4", "#A0E6E6", "#FF99CC", "#FFD580"];


        new Chart(this.chartRef.el, {
            type: "line",
            data: {
                labels,
                datasets: [{
                    label: "Top 5 Customers",
                    data,
                    borderColor: "#CDA0E6",
                    fill: false,

                }],
            },
            options: { responsive: true },
        });
    }
}


VehicleChartRendorBar.template = "owl.VehicleChartRendorBar";
VehicleChartRendorpie.template = "owl.VehicleChartRendorpie"
VehicleChartRendorline.template = "owl.VehicleChartRendorline"
VehicleChartRendordoughnut.template = "owl.VehicleChartRendordoughnut"



// Top 5 products all charts



// line chart
export class ProductLine extends Component {
    setup() {
        this.chartRef = useRef("chart");
        this.orm = useService("orm");
        onWillStart(async () => {
            await loadJS("https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.3.0/chart.umd.min.js");
        });

        onMounted(async () => await this.renderChart());
    }

    async renderChart() {
        const saleOrderLines = await this.orm.searchRead("sale.order.line", [], ["product_id"]);

        const productOrderCounts = saleOrderLines.reduce((count, orderLine) => {
            const productId = orderLine.product_id[0];
            count[productId] = (count[productId] || 0) + 1;
            return count;
        }, {});
        console.log("\n\n\n\n....productOrderCounts..", productOrderCounts);

        const topProducts = Object.entries(productOrderCounts)
            .sort((a, b) => b[1] - a[1])
            .slice(0, 5)
            .map(async ([productId]) => {
                const product = await this.orm.searchRead("product.product", [['id', '=', productId]], ['name']);
                console.log("\n\n\n....product.....", product);

                return { id: productId, name: product[0]?.name || 'Unknown', orders: productOrderCounts[productId] };
            });

        const productData = await Promise.all(topProducts);

        const labels = productData.map(product => product.name);
        const data = productData.map(product => product.orders);

        const ctx = this.chartRef.el.getContext("2d");
        new Chart(ctx, {
            type: "line",
            data: {
                labels,
                datasets: [{
                    label: "Top 5 Products Sales",
                    data,
                    backgroundColor: "rgba(0, 0, 255, 0.2)",
                    fill: false
                }]
            },
            options: {
                responsive: true,
                scales: {
                    y: { beginAtZero: true }
                }
            }
        });
    }
}


export class ProductBar extends Component {
    setup() {
        this.chartRef = useRef("chart");
        this.orm = useService("orm");
        onWillStart(async () => {
            await loadJS("https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.3.0/chart.umd.min.js");
        });

        onMounted(async () => await this.renderChart());
    }

    async renderChart() {
        const saleOrderLines = await this.orm.searchRead("sale.order.line", [], ["product_id"]);

        const productOrderCounts = saleOrderLines.reduce((count, orderLine) => {
            const productId = orderLine.product_id[0];
            count[productId] = (count[productId] || 0) + 1;
            return count;
        }, {});

        console.log("\n\n\n\n....productOrderCounts..", productOrderCounts);

        const topProducts = Object.entries(productOrderCounts)
            .sort((a, b) => b[1] - a[1])
            .slice(0, 5)
            .map(async ([productId]) => {
                const product = await this.orm.searchRead("product.product", [['id', '=', productId]], ['name']);
                console.log("\n\n\n....product.....", product);

                return { id: productId, name: product[0]?.name || 'Unknown', orders: productOrderCounts[productId] };
            });

        const productData = await Promise.all(topProducts);

        const labels = productData.map(product => product.name);
        const data = productData.map(product => product.orders);


        const backgroundColors = [
            "rgba(255, 182, 193, 0.5)",
            "rgba(216, 191, 216, 0.5)",
            "rgba(135, 206, 250, 0.5)",
            "rgba(255, 255, 224, 0.5)",
            "rgba(173, 216, 230, 0.5)"
        ];


        const ctx = this.chartRef.el.getContext("2d");
        new Chart(ctx, {
            type: "bar",
            data: {
                labels,
                datasets: [{
                    label: "Top 5 Products Sales",
                    data,
                    backgroundColor: backgroundColors.slice(0, data.length), // Assign colors dynamically
                    // borderColor: "rgba(0, 0, 0, 0.8)",
                    hoverBackgroundColor: backgroundColors // Prevent darkening on hover
                    // borderWidth: 1
                }]
            },
            options: {
                responsive: true,
                scales: {
                    y: { beginAtZero: true }
                }
            }
        });
    }
}


export class Productpie extends Component {
    setup() {
        this.chartRef = useRef("chart");
        this.orm = useService("orm");
        onWillStart(async () => {
            await loadJS("https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.3.0/chart.umd.min.js");
        });

        onMounted(async () => await this.renderChart());
    }

    async renderChart() {
        const saleOrderLines = await this.orm.searchRead("sale.order.line", [], ["product_id"]);

        const productOrderCounts = saleOrderLines.reduce((count, orderLine) => {
            const productId = orderLine.product_id[0];
            count[productId] = (count[productId] || 0) + 1;
            return count;
        }, {});

        console.log("\n\n\n\n....productOrderCounts..", productOrderCounts);

        const topProducts = Object.entries(productOrderCounts)
            .sort((a, b) => b[1] - a[1])
            .slice(0, 5)
            .map(async ([productId]) => {
                const product = await this.orm.searchRead("product.product", [['id', '=', productId]], ['name']);
                console.log("\n\n\n....product.....", product);

                return { id: productId, name: product[0]?.name || 'Unknown', orders: productOrderCounts[productId] };
            });

        const productData = await Promise.all(topProducts);

        const labels = productData.map(product => product.name);
        const data = productData.map(product => product.orders);

        // Define exactly 5 light-dark color pairs (same as Bar chart)

        const backgroundColors = [
            "rgba(255, 182, 193, 0.5)",
            "rgba(216, 191, 216, 0.5)",
            "rgba(135, 206, 250, 0.5)",
            "rgba(255, 255, 224, 0.5)",
            "rgba(173, 216, 230, 0.5)"
        ].slice(0, data.length);


        const ctx = this.chartRef.el.getContext("2d");
        new Chart(ctx, {
            type: "pie",
            data: {
                labels,
                datasets: [{
                    label: "Top 5 Products Sales",
                    data,
                    backgroundColor: backgroundColors, // Same colors as bar chart
                    borderColor: "rgba(0, 0, 0, 0.8)",
                    borderWidth: 1
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false
            }
        });
    }
}

export class Productdoughnut extends Component {
    setup() {
        this.chartRef = useRef("chart");
        this.orm = useService("orm");
        onWillStart(async () => {
            await loadJS("https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.3.0/chart.umd.min.js");
        });

        onMounted(async () => await this.renderChart());
    }

    async renderChart() {
        const saleOrderLines = await this.orm.searchRead("sale.order.line", [], ["product_id"]);

        const productOrderCounts = saleOrderLines.reduce((count, orderLine) => {
            const productId = orderLine.product_id[0];
            count[productId] = (count[productId] || 0) + 1;
            return count;
        }, {});

        console.log("\n\n\n\n....productOrderCounts..", productOrderCounts);

        const topProducts = Object.entries(productOrderCounts)
            .sort((a, b) => b[1] - a[1])
            .slice(0, 5)
            .map(async ([productId]) => {
                const product = await this.orm.searchRead("product.product", [['id', '=', productId]], ['name']);
                console.log("\n\n\n....product.....", product);

                return { id: productId, name: product[0]?.name || 'Unknown', orders: productOrderCounts[productId] };
            });

        const productData = await Promise.all(topProducts);

        const labels = productData.map(product => product.name);
        const data = productData.map(product => product.orders);

        // Define exactly 5 light-dark color pairs (same as Bar & Pie chart)
        const backgroundColors = [
            "rgba(255, 182, 193, 0.5)",
            "rgba(216, 191, 216, 0.5)",
            "rgba(135, 206, 250, 0.5)",
            "rgba(255, 255, 224, 0.5)",
            "rgba(173, 216, 230, 0.5)"
        ].slice(0, data.length);

        const ctx = this.chartRef.el.getContext("2d");
        new Chart(ctx, {
            type: "doughnut",
            data: {
                labels,
                datasets: [{
                    label: "Top 5 Products Sales",
                    data,
                    backgroundColor: backgroundColors, // Same colors as other charts
                    borderColor: "rgba(0, 0, 0, 0.8)",
                    borderWidth: 1
                }]
            },
            options: {
                responsive: true
            }
        });
    }
}

ProductLine.template = "owl.ProductLine";
ProductBar.template = "owl.ProductBar"
Productpie.template = "owl.Productpie"
Productdoughnut.template = "owl.Productdoughnut"